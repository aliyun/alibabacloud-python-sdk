# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySslVpnServerRequest(DaraModel):
    def __init__(
        self,
        cipher: str = None,
        client_ip_pool: str = None,
        client_token: str = None,
        compress: bool = None,
        dns_servers: str = None,
        dry_run: bool = None,
        enable_multi_factor_auth: bool = None,
        idaa_sapplication_id: str = None,
        idaa_sinstance_id: str = None,
        idaa_sregion_id: str = None,
        local_subnet: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        port: int = None,
        proto: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        ssl_vpn_server_id: str = None,
    ):
        # The encryption algorithm used by SSL-VPN. Valid values:
        # 
        # - **AES-128-CBC** (default): AES-128-CBC algorithm.
        # 
        # - **AES-192-CBC**: AES-192-CBC algorithm.
        # 
        # - **AES-256-CBC**: AES-256-CBC algorithm.
        # 
        # - **none**: No encryption algorithm is used.
        self.cipher = cipher
        # The client CIDR block.
        # 
        # This is the CIDR block used to allocate IP addresses to the virtual network interface of the client, not the existing internal CIDR block of the client.
        # 
        # When the client accesses the local end through an SSL-VPN connection, the VPN gateway allocates an IP address from the specified client CIDR block to the client. The client uses the allocated IP address to access cloud resources.
        # 
        # When you specify the client CIDR block, make sure that the number of IP addresses in the client CIDR block is at least four times the number of SSL connections of the current VPN gateway.
        # <details>
        # <summary>Click to view the reason.</summary>
        # For example, if the client CIDR block you specify is 192.168.0.0/24, when the system allocates IP addresses to the client, it first divides a subnet with a 30-bit subnet mask from the 192.168.0.0/24 CIDR block, such as 192.168.0.4/30, and then allocates one IP address from 192.168.0.4/30 for the client to use. The remaining three IP addresses are occupied by the system to ensure network communication. In this case, one client consumes 4 IP addresses. Therefore, to ensure that all your clients can be allocated IP addresses, make sure that the number of IP addresses in the client CIDR block you specify is at least four times the number of SSL connections of the VPN gateway.
        # </details>
        # 
        # <details>
        # <summary>Click to view unsupported CIDR blocks.</summary>
        # 
        # - 100.64.0.0~100.127.255.255
        # - 127.0.0.0~127.255.255.255
        # - 169.254.0.0~169.254.255.255
        # - 224.0.0.0~239.255.255.255
        # - 255.0.0.0~255.255.255.255
        # 
        # </details>
        # 
        # <details>
        # <summary>Click to view recommended client CIDR blocks for each SSL connection count.</summary>
        # 
        # - If the number of SSL connections is 5, the subnet mask of the client CIDR block should be less than or equal to 27 bits. For example: 10.0.0.0/27 or 10.0.0.0/26.
        # - If the number of SSL connections is 10, the subnet mask of the client CIDR block should be less than or equal to 26 bits. For example: 10.0.0.0/26 or 10.0.0.0/25.
        # - If the number of SSL connections is 20, the subnet mask of the client CIDR block should be less than or equal to 25 bits. For example: 10.0.0.0/25 or 10.0.0.0/24.
        # - If the number of SSL connections is 50, the subnet mask of the client CIDR block should be less than or equal to 24 bits. For example: 10.0.0.0/24 or 10.0.0.0/23.
        # - If the number of SSL connections is 100, the subnet mask of the client CIDR block should be less than or equal to 23 bits. For example: 10.0.0.0/23 or 10.0.0.0/22.
        # - If the number of SSL connections is 200, the subnet mask of the client CIDR block should be less than or equal to 22 bits. For example: 10.0.0.0/22 or 10.0.0.0/21.
        # - If the number of SSL connections is 500, the subnet mask of the client CIDR block should be less than or equal to 21 bits. For example: 10.0.0.0/21 or 10.0.0.0/20.
        # - If the number of SSL connections is 1000, the subnet mask of the client CIDR block should be less than or equal to 20 bits. For example: 10.0.0.0/20 or 10.0.0.0/19.
        # 
        # </details>
        # 
        # > - The subnet mask of the client CIDR block must be between 16 and 29 bits.
        # > - Make sure that the client CIDR block does not overlap with the local subnet, VPC CIDR block, or any route CIDR blocks associated with the client terminal.
        # > - When specifying the client CIDR block, we recommend that you use the 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16 CIDR blocks and their subnets. If you need to specify a public CIDR block as the client CIDR block, you must set the public CIDR block as a user CIDR block of the VPC to ensure that the VPC can access the public CIDR block. For more information about user CIDR blocks, see [VPC FAQ](https://help.aliyun.com/document_detail/185311.html).
        # > - After the SSL server is created, the system automatically adds routes for the client CIDR block to the route table of the VPC instance. Do not manually add routes for the client CIDR block to the route table of the VPC instance. Otherwise, SSL-VPN connection traffic transmission will be abnormal.
        self.client_ip_pool = client_ip_pool
        # The client token that is used to ensure the idempotency of the request.
        # 
        # Generate a parameter value from your client to ensure uniqueness across different requests. ClientToken supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is different.
        self.client_token = client_token
        # Specifies whether to compress the communication. Valid values:
        # 
        # - **true** (default): Compresses the communication.
        # 
        # - **false**: Does not compress the communication.
        self.compress = compress
        self.dns_servers = dns_servers
        # Specifies whether to perform only a dry run, without actually modifying the configuration. Valid values:
        # - **true**: Sends a check request without modifying the SSL server configuration. The check items include whether all required parameters are specified, request format, and service limits. If the check fails, the corresponding error is returned. If the check passes, the error code `DryRunOperation` is returned.
        # - **false** (default): Sends a normal request. After the check passes, an HTTP 2xx status code is returned, and the operation is performed.
        self.dry_run = dry_run
        # Specifies whether to enable two-factor authentication. If you choose to enable two-factor authentication, you also need to configure **IDaaSInstanceId**, **IDaaSRegionId**, and **IDaaSApplicationId**. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Not enabled.
        # 
        # >- If you are using the two-factor authentication feature for the first time, complete the [authorization](https://ram.console.aliyun.com/role/authorization?request=%7B%22Services%22%3A%5B%7B%22Service%22%3A%22VPN%22%2C%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunVpnAccessingIdaasRole%22%2C%22TemplateId%22%3A%22IdaasRole%22%7D%5D%7D%5D%2C%22ReturnUrl%22%3A%22https%3A%2F%2Fvpc.console.aliyun.com%2Fsslvpn%2Fcn-shanghai%2Fvpn-servers%22%7D) before creating the SSL server.
        # >- When creating an SSL server in the UAE (Dubai) region, we recommend that you bind an IDaaS EIAM 2.0 instance in the Singapore region to reduce cross-region latency.
        # >- IDaaS EIAM 1.0 instances are no longer available for purchase. If your Alibaba Cloud account has existing IDaaS EIAM 1.0 instances, you can still bind them after enabling two-factor authentication. If your Alibaba Cloud account does not have IDaaS EIAM 1.0 instances, only IDaaS EIAM 2.0 instances can be bound after enabling two-factor authentication.
        self.enable_multi_factor_auth = enable_multi_factor_auth
        # The ID of the IDaaS application.
        # 
        # - If you bind an IDaaS EIAM 2.0 instance, you must enter the IDaaS application ID.
        # - If you bind an IDaaS EIAM 1.0 instance, you do not need to enter the IDaaS application ID.
        self.idaa_sapplication_id = idaa_sapplication_id
        # The ID of the IDaaS EIAM instance.
        self.idaa_sinstance_id = idaa_sinstance_id
        # The region ID of the IDaaS EIAM instance.
        self.idaa_sregion_id = idaa_sregion_id
        # The local subnet.
        # 
        # The CIDR block that the client needs to access through the SSL-VPN connection.
        # 
        # The local subnet can be the CIDR block of a VPC, a vSwitch, an IDC interconnected with the VPC through Express Connect, or a cloud service such as Object Storage Service (OSS).
        # 
        # The subnet mask of the local subnet must be between 8 and 32 bits. The following CIDR blocks cannot be specified as local subnets:
        # 
        # - 127.0.0.0~127.255.255.255
        # - 169.254.0.0~169.254.255.255
        # - 224.0.0.0~239.255.255.255
        # - 255.0.0.0~255.255.255.255
        self.local_subnet = local_subnet
        # The name of the SSL-VPN server.
        # 
        # The name must be 1 to 100 characters in length and cannot start with `http://` or `https://`.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The port used by the SSL-VPN server. Valid values: **1** to **65535**. Default value: **1194**.
        # 
        # The following ports are not supported: **22**, **2222**, **22222**, **9000**, **9001**, **9002**, **7505**, **80**, **443**, **53**, **68**, **123**, **4510**, **4560**, **500**, and **4500**.
        self.port = port
        # The protocol used by the SSL-VPN server. Valid values:
        # 
        # - **TCP** (default): TCP protocol.
        # 
        # - **UDP**: UDP protocol.
        self.proto = proto
        # The region ID of the VPN gateway.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the SSL-VPN server instance.
        # 
        # This parameter is required.
        self.ssl_vpn_server_id = ssl_vpn_server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cipher is not None:
            result['Cipher'] = self.cipher

        if self.client_ip_pool is not None:
            result['ClientIpPool'] = self.client_ip_pool

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.compress is not None:
            result['Compress'] = self.compress

        if self.dns_servers is not None:
            result['DnsServers'] = self.dns_servers

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.enable_multi_factor_auth is not None:
            result['EnableMultiFactorAuth'] = self.enable_multi_factor_auth

        if self.idaa_sapplication_id is not None:
            result['IDaaSApplicationId'] = self.idaa_sapplication_id

        if self.idaa_sinstance_id is not None:
            result['IDaaSInstanceId'] = self.idaa_sinstance_id

        if self.idaa_sregion_id is not None:
            result['IDaaSRegionId'] = self.idaa_sregion_id

        if self.local_subnet is not None:
            result['LocalSubnet'] = self.local_subnet

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.port is not None:
            result['Port'] = self.port

        if self.proto is not None:
            result['Proto'] = self.proto

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.ssl_vpn_server_id is not None:
            result['SslVpnServerId'] = self.ssl_vpn_server_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cipher') is not None:
            self.cipher = m.get('Cipher')

        if m.get('ClientIpPool') is not None:
            self.client_ip_pool = m.get('ClientIpPool')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Compress') is not None:
            self.compress = m.get('Compress')

        if m.get('DnsServers') is not None:
            self.dns_servers = m.get('DnsServers')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EnableMultiFactorAuth') is not None:
            self.enable_multi_factor_auth = m.get('EnableMultiFactorAuth')

        if m.get('IDaaSApplicationId') is not None:
            self.idaa_sapplication_id = m.get('IDaaSApplicationId')

        if m.get('IDaaSInstanceId') is not None:
            self.idaa_sinstance_id = m.get('IDaaSInstanceId')

        if m.get('IDaaSRegionId') is not None:
            self.idaa_sregion_id = m.get('IDaaSRegionId')

        if m.get('LocalSubnet') is not None:
            self.local_subnet = m.get('LocalSubnet')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Proto') is not None:
            self.proto = m.get('Proto')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SslVpnServerId') is not None:
            self.ssl_vpn_server_id = m.get('SslVpnServerId')

        return self

