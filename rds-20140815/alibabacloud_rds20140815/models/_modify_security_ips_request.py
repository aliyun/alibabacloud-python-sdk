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
        # - If you do not specify this parameter, the group is a regular group. This is the default value.
        # - If you set this parameter to `hidden`, the group is a hidden group that is automatically created by the system for services such as DMS, DTS, and DAS. Hidden groups are not displayed in the console. If you delete or modify a hidden group, services such as DMS, DTS, and DAS cannot access the ApsaraDB RDS instance. Proceed with caution.
        self.dbinstance_iparray_attribute = dbinstance_iparray_attribute
        # The name of the IP address whitelist group to be modified. Default value: Default. If the specified group does not exist, the system automatically creates the group.
        # 
        # >You can create up to 200 whitelist groups for a single instance.
        self.dbinstance_iparray_name = dbinstance_iparray_name
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The read-only instances to which the whitelist is synchronized.
        # 
        # - This parameter is applicable only to ApsaraDB RDS for PostgreSQL instances that have read-only instances.
        # - If multiple read-only instances exist, separate their IDs with commas (,).
        self.fresh_white_list_readins = fresh_white_list_readins
        # The modification mode. Valid values:
        # * **Cover**: overwrites the original IP address whitelist with the IP addresses specified by the **SecurityIps** parameter. This is the default value.
        # * **Append**: appends the IP addresses specified by the **SecurityIps** parameter to the original IP address whitelist.
        # * **Delete**: deletes the IP addresses specified by the **SecurityIps** parameter from the original IP address whitelist. You must retain at least one IP address in the whitelist.
        self.modify_mode = modify_mode
        self.resource_owner_id = resource_owner_id
        # The type of the IP address. Set the value to IPv4. IPv6 is not supported.
        self.security_iptype = security_iptype
        # The IP address whitelist. Before you modify the IP address whitelist, call the [DescribeDBInstanceIPArrayList](https://help.aliyun.com/document_detail/610518.html) operation to query the existing IP address whitelist of the instance.
        # 
        # <details>
        # <summary>Configuration rules</summary>
        # 
        # - You can enter IP addresses (such as 10.23.XX.XX) or CIDR blocks (such as 10.23.XX.XX/24).
        # 
        # - Separate multiple IP addresses or CIDR blocks with commas (,). Do not add spaces before or after the commas.
        # 
        # - You can add up to 1,000 IP addresses or CIDR blocks to the whitelist of a single instance. If you have a large number of IP addresses, we recommend that you merge them into CIDR blocks, such as 10.23.XX.XX/24.
        # </details>
        # 
        # This parameter is required.
        self.security_ips = security_ips
        # The network type of the whitelist. Valid values:
        # 
        # * **MIX**: the general mode. This is the default value.
        # * **Classic**: the classic network in the enhanced whitelist mode.
        # * **VPC**: the VPC in the enhanced whitelist mode.
        # 
        # > * For ApsaraDB RDS for PostgreSQL instances with cloud disks, the network type is fixed to the general mode (MIX). If you configure another mode, the system automatically changes it to the general mode.
        # > * The enhanced whitelist mode is supported only by ApsaraDB RDS for MySQL 5.1, 5.5, 5.6, and 5.7 instances with premium local SSDs, and ApsaraDB RDS for PostgreSQL 9.4 and 10 instances with premium local SSDs.
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

