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
        # The attribute of the IP address whitelist. By default, this parameter is empty.
        # 
        # > The IP address whitelists that have the hidden attribute are not displayed in the ApsaraDB RDS console. These IP address whitelists are used to access Alibaba Cloud services, such as Data Transmission Service (DTS).
        self.dbinstance_iparray_attribute = dbinstance_iparray_attribute
        # The name of the IP address whitelist that you want to modify. Default value: **Default**.
        # 
        # > A maximum of 200 IP address whitelists can be configured for each instance.
        self.dbinstance_iparray_name = dbinstance_iparray_name
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The read-only instances to which you want to synchronize the IP address whitelist.
        # 
        # *   This parameter applies only to ApsaraDB RDS for PostgreSQL instances.
        # *   If the instance is attached with a read-only instance, you can use this parameter to synchronize the IP address whitelist to the read-only instance. If the instance is attached with multiple read-only instances, separate the read-only instances with commas (,).
        # *   If the instance is not attached with a read-only instance, leave this parameter empty.
        self.fresh_white_list_readins = fresh_white_list_readins
        # The method that is used to modify the whitelist. Valid values:
        # 
        # *   **Cover**: Use the IP addresses and CIDR blocks that are specified in the **SecurityIps** parameter to overwrite the existing IP addresses and CIDR blocks in the IP address whitelist.
        # *   **Append**: Add the IP addresses and CIDR blocks that are specified in the **SecurityIps** parameter to the IP address whitelist.
        # *   **Delete**: Delete the IP addresses and CIDR blocks that are specified in the **SecurityIps** parameter from the IP address whitelist. You must retain at least one IP address or CIDR block.
        # 
        # Default value: **Cover**.
        self.modify_mode = modify_mode
        self.resource_owner_id = resource_owner_id
        # The IP address type. The value is fixed as IPv4.
        self.security_iptype = security_iptype
        # The IP addresses in an IP address whitelist. Separate multiple IP addresses with commas (,). Each IP address in the IP address whitelist must be unique. The entries in the IP address whitelist must be in one of the following formats:
        # 
        # *   IP addresses, such as 10.23.XX.XX.
        # *   CIDR blocks, such as 10.23.XX.XX/24. In this example, 24 indicates that the prefix of each IP address in the IP address whitelist is 24 bits in length. You can replace 24 with a value within the range of 1 to 32.
        # 
        # > A maximum of 1,000 IP addresses or CIDR blocks can be added for each instance. If you want to add a large number of IP addresses, we recommend that you merge them into CIDR blocks, such as 10.23.XX.XX/24.
        # 
        # This parameter is required.
        self.security_ips = security_ips
        # The network type of the IP address whitelist. Valid values:
        # 
        # *   **Classic**: classic network in enhanced whitelist mode
        # *   **VPC**: virtual private cloud (VPC) network type in enhanced whitelist mode.
        # *   **MIX**: standard whitelist mode
        # 
        # Default value: **MIX**.
        # 
        # > 
        # 
        # *   In standard whitelist mode, IP addresses and CIDR blocks are added only to the default IP address whitelist. In enhanced whitelist mode, IP addresses and CIDR blocks are added to the IP address whitelists of the classic network type and the VPC network type.
        # 
        # *   If your RDS instance runs PostgreSQL and uses cloud disks, set this parameter to MIX. If you set it to another value, the system automatically changes the value to MIX.
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

