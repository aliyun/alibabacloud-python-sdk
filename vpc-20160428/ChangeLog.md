2025-08-28 Version: 6.12.0
- Support API DescribeVpcGrantRulesToEcr.
- Update API CreateNatGateway: add request parameters Ipv4Prefix.
- Update API CreateNatGateway: add request parameters NatIp.
- Update API CreateNatIp: add request parameters Ipv4Prefix.
- Update API CreateNatIp: add request parameters Ipv4PrefixCount.
- Update API CreateNatIp: add response parameters Body.Ipv4Prefix.
- Update API DeleteNatIp: add request parameters Ipv4Prefix.
- Update API DeleteNatIp: add request parameters NatGatewayId.
- Update API DescribeNatGateways: add response parameters Body.NatGateways.$.IpPrefixList.
- Update API ListNatIps: add response parameters Body.NatIps.$.Ipv4Prefix.


2025-07-24 Version: 6.11.9
- Update API AssociateVpcCidrBlock: add request parameters Ipv6CidrMask.
- Update API CreateVpc: add request parameters Ipv6CidrMask.
- Update API CreateVpc: add request parameters Ipv6IpamPoolId.


2025-07-15 Version: 6.11.8
- Update API DescribeNatGatewayAssociateNetworkInterfaces: add response parameters Body.AssociateNetworkInterfaces.$.ResourceVpcId.
- Update API GetVpcPrefixListAssociations: add response parameters Body.PrefixListAssociation.$.CidrList.


2025-06-16 Version: 6.11.7
- Update API GetDhcpOptionsSet: add response parameters Body.CreationTime.
- Update API ListDhcpOptionsSets: add response parameters Body.DhcpOptionsSets.$.CreationTime.


2025-06-16 Version: 6.11.6
- Update API CreateRouteEntries: add request parameters DryRun.
- Update API CreateRouteEntry: add request parameters DryRun.
- Update API CreateSslVpnServer: add request parameters DryRun.
- Update API CreateTrafficMirrorFilter: add request parameters EgressRules.$.IpVersion.
- Update API CreateTrafficMirrorFilter: add request parameters IngressRules.$.IpVersion.
- Update API CreateTrafficMirrorFilterRules: add request parameters EgressRules.$.IpVersion.
- Update API CreateTrafficMirrorFilterRules: add request parameters IngressRules.$.IpVersion.
- Update API CreateVcoRouteEntry: add request parameters DryRun.
- Update API CreateVpnAttachment: add request parameters DryRun.
- Update API CreateVpnConnection: add request parameters DryRun.
- Update API CreateVpnPbrRouteEntry: add request parameters DryRun.
- Update API CreateVpnRouteEntry: add request parameters DryRun.
- Update API DeleteRouteEntries: add request parameters DryRun.
- Update API DeleteRouteEntry: add request parameters DryRun.
- Update API DownloadVpnConnectionConfig: add response parameters Body.VpnConnectionConfig.BgpConfigs.
- Update API ListTrafficMirrorFilters: add response parameters Body.TrafficMirrorFilters.$.EgressRules.$.IpVersion.
- Update API ListTrafficMirrorFilters: add response parameters Body.TrafficMirrorFilters.$.IngressRules.$.IpVersion.
- Update API ListVpcGatewayEndpoints: add request parameters VpcId.
- Update API ModifyRouteEntry: add request parameters DryRun.
- Update API ModifySslVpnServer: add request parameters DryRun.


2025-04-14 Version: 6.11.5
- Update API DescribeIpv6GatewayAttribute: add response parameters Body.OwnerId.
- Update API DescribeIpv6Gateways: add response parameters Body.Ipv6Gateways.$.OwnerId.


2025-04-01 Version: 6.11.4
- Update API DeleteVSwitch: add request parameters DryRun.


2025-03-26 Version: 6.11.3
- Update API AllocateEipAddress: add request parameters Tag.
- Update API AllocateEipAddressPro: add request parameters Tag.
- Update API CreateCommonBandwidthPackage: add request parameters Tag.


2025-02-27 Version: 6.11.2
- Generated python 2016-04-28 for Vpc.

2025-02-26 Version: 6.11.1
- Update API DescribeFlowLogs: update response param.


2025-02-21 Version: 6.11.0
- Support API ModifyEipForwardMode.
- Update API AssociateVpcCidrBlock: update response param.
- Update API CreateFlowLog: add param TrafficAnalyzerId.
- Update API CreateFlowLog: update param LogStoreName.
- Update API CreateFlowLog: update param ProjectName.
- Update API CreateRouteEntries: update param RouteEntries.
- Update API DeleteRouteEntries: update param RouteEntries.
- Update API DeleteVSwitch: update response param.
- Update API DeletionProtection: update response param.
- Update API DescribeEipAddresses: update response param.
- Update API DescribeFlowLogs: update response param.
- Update API DescribeIpv6Gateways: update response param.
- Update API DescribeRouteEntryList: update param DestCidrBlockList.
- Update API GetIpv4GatewayAttribute: update response param.
- Update API ListDhcpOptionsSets: update response param.
- Update API ListTrafficMirrorSessions: update response param.
- Update API ModifyFlowLogAttribute: add param DisableLogDelivery.
- Update API ModifyFlowLogAttribute: add param EnableTrafficAnalyze.
- Update API ModifyFlowLogAttribute: add param TrafficAnalyzerId.


2024-12-30 Version: 6.10.1
- Update API DescribeNatGatewayAssociateNetworkInterfaces: update response param.


2024-12-20 Version: 6.10.0
- Support API TransformEipSegmentToPublicIpAddressPool.


2024-12-18 Version: 6.9.6
- Update API CreateExpressConnectTrafficQos: add param ResourceGroupId.
- Update API CreateExpressConnectTrafficQos: add param Tags.
- Update API CreateForwardEntry: add param DryRun.
- Update API CreateSnatEntry: add param DryRun.
- Update API CreateVpnAttachment: add param EnableTunnelsBgp.
- Update API CreateVpnAttachment: add param TunnelOptionsSpecification.
- Update API CreateVpnAttachment: update param CustomerGatewayId.
- Update API CreateVpnAttachment: update param RemoteCaCert.
- Update API DescribeExpressConnectTrafficQos: add param ResourceGroupId.
- Update API DescribeExpressConnectTrafficQos: add param Tags.
- Update API DescribeExpressConnectTrafficQos: update response param.
- Update API DescribeVcoRouteEntries: update response param.
- Update API DescribeVpnAttachments: update response param.
- Update API DescribeVpnConnection: update response param.
- Update API DescribeVpnConnections: update response param.
- Update API DescribeVpnRouteEntries: update response param.
- Update API ModifyForwardEntry: add param DryRun.
- Update API ModifyForwardEntry: update response param.
- Update API ModifyRouteEntry: update param RouteEntryId.
- Update API ModifySnatEntry: add param DryRun.
- Update API ModifyTunnelAttribute: update param TunnelOptionsSpecification.
- Update API ModifyVpnAttachmentAttribute: add param EnableTunnelsBgp.
- Update API ModifyVpnAttachmentAttribute: add param TunnelOptionsSpecification.
- Update API ModifyVpnAttachmentAttribute: update param RemoteCaCert.
- Update API ModifyVpnAttachmentAttribute: update response param.
- Update API ModifyVpnConnectionAttribute: update param TunnelOptionsSpecification.


2024-11-29 Version: 6.9.5
- Update API CreateVpnAttachment: add param EnableTunnelsBgp.
- Update API CreateVpnAttachment: add param TunnelOptionsSpecification.
- Update API CreateVpnAttachment: update param CustomerGatewayId.
- Update API CreateVpnAttachment: update param RemoteCaCert.
- Update API DescribeVcoRouteEntries: update response param.
- Update API DescribeVpnAttachments: update response param.
- Update API DescribeVpnConnection: update response param.
- Update API DescribeVpnConnections: update response param.
- Update API DescribeVpnRouteEntries: update response param.
- Update API ModifyRouteEntry: update param RouteEntryId.
- Update API ModifyTunnelAttribute: update param TunnelOptionsSpecification.
- Update API ModifyVpnAttachmentAttribute: add param EnableTunnelsBgp.
- Update API ModifyVpnAttachmentAttribute: add param TunnelOptionsSpecification.
- Update API ModifyVpnAttachmentAttribute: update param RemoteCaCert.
- Update API ModifyVpnAttachmentAttribute: update response param.
- Update API ModifyVpnConnectionAttribute: update param TunnelOptionsSpecification.


2024-10-24 Version: 6.9.4
- Update API CreateFlowLog: add param IpVersion.
- Update API CreateNatGateway: add param AccessMode.
- Update API CreateNatGateway: add param PrivateLinkEnabled.
- Update API DescribeFlowLogs: update response param.
- Update API DescribeNatGatewayAssociateNetworkInterfaces: update response param.
- Update API DescribeNatGateways: update response param.
- Update API GetNatGatewayAttribute: update response param.
- Update API ModifyFlowLogAttribute: add param IpVersion.


2024-09-14 Version: 6.9.3
- Update API ListVpcPublishedRouteEntries: update response param.


2024-08-29 Version: 6.9.2
- Update API ModifyRouteEntry: add param DestinationCidrBlock.
- Update API ModifyRouteEntry: add param RouteTableId.
- Update API ModifyRouteEntry: update param RouteEntryId.


2024-08-27 Version: 6.9.1
- Update API CreateVpc: add param EnableDnsHostname.
- Update API DescribeVpcAttribute: update response param.
- Update API DescribeVpcs: update response param.
- Update API ModifyVpcAttribute: add param EnableDnsHostname.


2024-08-19 Version: 6.9.0
- Support API ListVpcPublishedRouteEntries.
- Support API PublishVpcRouteEntries.
- Support API WithdrawVpcPublishedRouteEntries.
- Update API DescribeEcGrantRelation: update response param.


2024-08-15 Version: 6.8.0
- Support API DescribeNatGatewayAssociateNetworkInterfaces.


2024-08-09 Version: 6.7.4
- Update API CreateSnatEntry: add param NetworkInterfaceId.
- Update API CreateSnatEntry: update param SnatIp.
- Update API DescribeSnatTableEntries: add param NetworkInterfaceIds.
- Update API DescribeSnatTableEntries: update response param.
- Update API ModifySnatEntry: add param NetworkInterfaceId.


2024-08-08 Version: 6.7.3
- Update API ListPublicIpAddressPools: update response param.
- Update API UpdateVirtualPhysicalConnection: update response param.


2024-07-24 Version: 6.7.2
- Update API AllocateIpv6InternetBandwidth: add param DryRun.
- Update API AllocateIpv6InternetBandwidth: update param ClientToken.
- Update API DeleteIpv6Gateway: add param ClientToken.
- Update API DeleteIpv6Gateway: add param DryRun.
- Update API DeleteIpv6InternetBandwidth: add param ClientToken.
- Update API DeleteIpv6InternetBandwidth: add param DryRun.
- Update API DeleteVSwitchCidrReservation: add param ClientToken.
- Update API DeleteVSwitchCidrReservation: add param DryRun.
- Update API DeleteVpc: add param ClientToken.
- Update API DeleteVpc: update response param.
- Update API DescribePublicIpAddress: add param IpVersion.
- Update API ModifyFullNatEntryAttribute: update response param.
- Update API ModifyIpv6AddressAttribute: add param ClientToken.
- Update API ModifyIpv6AddressAttribute: add param DryRun.
- Update API ModifyIpv6GatewayAttribute: add param ClientToken.
- Update API ModifyIpv6GatewayAttribute: add param DryRun.
- Update API ModifyIpv6InternetBandwidth: add param DryRun.
- Update API ModifyIpv6InternetBandwidth: update param ClientToken.
- Update API ModifyVSwitchCidrReservationAttribute: add param ClientToken.
- Update API ModifyVSwitchCidrReservationAttribute: add param DryRun.


2024-07-19 Version: 6.7.1
- Update API CreateFailoverTestJob: add param DryRun.
- Update API CreateFailoverTestJob: update param ResourceType.
- Update API DescribeFailoverTestJob: update response param.
- Update API DescribeFailoverTestJobs: update response param.
- Update API UpdateFailoverTestJob: add param DryRun.


2024-06-28 Version: 6.7.0
- Support API GetPublicIpAddressPoolServiceStatus.
- Support API OpenPublicIpAddressPoolService.
- Update API AllocateIpv6Address: add param AddressType.
- Update API CreateBgpGroup: update response param.
- Update API DescribeIpv6Addresses: add param AddressType.
- Update API DescribeIpv6Addresses: update response param.
- Update API DescribeIpv6EgressOnlyRules: update response param.
- Update API ModifyBgpGroupAttribute: update response param.
- Update API ModifyRouteTableAttributes: add param RoutePropagationEnable.


2024-06-14 Version: 6.6.8
- Update API DeleteIpv4Gateway: add param InternetMode.


2024-06-06 Version: 6.6.7
- Update API CreateFullNatEntry: update param NatIpPort.
- Update API DeleteRouteEntry: update param RouteEntryId.
- Update API DeleteRouteEntry: update response param.


2024-05-27 Version: 6.6.6
- Update API ListPublicIpAddressPools: update response param.


2024-05-27 Version: 6.6.6
- Update API ListPublicIpAddressPools: update response param.


2024-05-16 Version: 6.6.5
- Update API DescribeVSwitches: add param EnableIpv6.
- Update API DescribeVpcs: add param EnableIpv6.


2024-05-10 Version: 6.6.4
- Update API CreateSslVpnServer: add param IDaaSApplicationId.
- Update API DescribeSslVpnServers: update response param.
- Update API ModifySslVpnServer: add param IDaaSApplicationId.
- Update API ModifySslVpnServer: update response param.


2024-05-10 Version: 6.6.4
- Update API CreateSslVpnServer: add param IDaaSApplicationId.
- Update API DescribeSslVpnServers: update response param.
- Update API ModifySslVpnServer: add param IDaaSApplicationId.
- Update API ModifySslVpnServer: update response param.


2024-05-07 Version: 6.6.3
- Update API DescribeNatGateways: update response param.
- Update API GetNatGatewayAttribute: update response param.
- Update API ModifyNatGatewayAttribute: add param EnableSessionLog.
- Update API ModifyNatGatewayAttribute: add param LogDelivery.


2024-05-06 Version: 6.6.2
- Update API DescribeSnatTableEntries: update response param.
- Update API DescribeVpnGateway: update response param.
- Update API DescribeVpnGateways: update response param.
- Update API ListTrafficMirrorFilters: update response param.
- Update API ModifySnatEntry: add param EipAffinity.


2024-04-25 Version: 6.6.1
- Update API AssociateVpcCidrBlock: add param SecondaryCidrMask.
- Update API CreateVpc: add param Ipv4CidrMask.


2024-04-17 Version: 6.6.0
- Support API CreateExpressConnectTrafficQos.
- Support API CreateExpressConnectTrafficQosQueue.
- Support API CreateExpressConnectTrafficQosRule.
- Support API DeleteExpressConnectTrafficQos.
- Support API DeleteExpressConnectTrafficQosQueue.
- Support API DeleteExpressConnectTrafficQosRule.
- Support API Describe95Traffic.
- Support API DescribeExpressConnectTrafficQos.
- Support API DescribeExpressConnectTrafficQosQueue.
- Support API DescribeExpressConnectTrafficQosRule.
- Support API ModifyExpressConnectTrafficQos.
- Support API ModifyExpressConnectTrafficQosQueue.
- Support API ModifyExpressConnectTrafficQosRule.
- Update API AddPublicIpAddressPoolCidrBlock: update response param.
- Update API CreatePublicIpAddressPool: update response param.
- Update API DescribeEipAddresses: add param ServiceManaged.
- Update API DescribeIpv6Addresses: add param ServiceManaged.
- Update API DescribeIpv6Addresses: update response param.
- Update API DescribePublicIpAddress: update response param.
- Update API DescribeVirtualBorderRouters: update response param.
- Update API DescribeVpcAttribute: update response param.
- Update API DescribeVpcs: update response param.


2024-04-17 Version: 6.5.0
- Support API CreateExpressConnectTrafficQos.
- Support API CreateExpressConnectTrafficQosQueue.
- Support API CreateExpressConnectTrafficQosRule.
- Support API DeleteExpressConnectTrafficQos.
- Support API DeleteExpressConnectTrafficQosQueue.
- Support API DeleteExpressConnectTrafficQosRule.
- Support API Describe95Traffic.
- Support API DescribeExpressConnectTrafficQos.
- Support API DescribeExpressConnectTrafficQosQueue.
- Support API DescribeExpressConnectTrafficQosRule.
- Support API ModifyExpressConnectTrafficQos.
- Support API ModifyExpressConnectTrafficQosQueue.
- Support API ModifyExpressConnectTrafficQosRule.
- Update API AddPublicIpAddressPoolCidrBlock: update response param.
- Update API CreatePublicIpAddressPool: update response param.
- Update API DescribeEipAddresses: add param ServiceManaged.
- Update API DescribeIpv6Addresses: add param ServiceManaged.
- Update API DescribeIpv6Addresses: update response param.
- Update API DescribePublicIpAddress: update response param.
- Update API DescribeVpcAttribute: update response param.
- Update API DescribeVpcs: update response param.


2024-02-01 Version: 6.4.0
- Support API AllocateIpv6Address.
- Support API ReleaseIpv6Address.
- Update API CreatePublicIpAddressPooladd SecurityProtectionTypes param.
- Update API CreateVpnPbrRouteEntryupdate response param.
- Update API DescribePhysicalConnectionsupdate response param.
- Update API DescribeRouteEntryListupdate response param.
- Update API DescribeRouteTableListupdate response param.
- Update API DescribeVpcAttributeupdate response param.
- Update API ListPublicIpAddressPoolsadd SecurityProtectionEnabled param.
update response param.
- Update API ModifyNatGatewayAttributeupdate response param.
- Update API ModifySnatEntryupdate response param.
- Update API ModifyTunnelAttributeupdate response param.
- Update API ModifyVpnConnectionAttributeupdate TunnelOptionsSpecification param.


2024-01-22 Version: 6.3.0
- Generated python 2016-04-28 for Vpc.

2023-12-29 Version: 6.2.2
- Generated python 2016-04-28 for Vpc.

2023-12-20 Version: 6.2.1
- Generated python 2016-04-28 for Vpc.

2023-12-19 Version: 6.2.0
- Generated python 2016-04-28 for Vpc.

2023-11-27 Version: 6.1.2
- Generated python 2016-04-28 for Vpc.

2023-11-25 Version: 6.1.1
- Generated python 2016-04-28 for Vpc.

2023-11-21 Version: 6.1.0
- Generated python 2016-04-28 for Vpc.

2023-10-21 Version: 6.0.2
- Generated python 2016-04-28 for Vpc.

2023-10-19 Version: 6.0.1
- Generated python 2016-04-28 for Vpc.

2023-10-18 Version: 6.0.0
- Generated python 2016-04-28 for Vpc.

2023-09-15 Version: 5.1.0
- Generated python 2016-04-28 for Vpc.

2023-09-07 Version: 5.0.2
- Generated python 2016-04-28 for Vpc.

2023-08-25 Version: 5.0.1
- Generated python 2016-04-28 for Vpc.

2023-08-18 Version: 5.0.0
- DescribeForwardTables offline.

2023-08-15 Version: 4.1.1
- Generated python 2016-04-28 for Vpc.

2023-08-15 Version: 4.1.1
- Generated python 2016-04-28 for Vpc.

2023-08-10 Version: 4.1.0
- Generated python 2016-04-28 for Vpc.

2023-08-09 Version: 4.0.2
- Generated python 2016-04-28 for Vpc.

2023-08-08 Version: 4.0.1
- Generated python 2016-04-28 for Vpc.

2023-08-07 Version: 4.0.0
- DescribeForwardTables offline.

2023-07-21 Version: 3.0.1
- Add error code.
- Add Deliver Param.
- Add errorcode.
- Support tags for CreateTrafficMirrorSession and CreatePublicIpAddressPool.
- VBR and RI support resource group and tags.
- Api Type Tag.
- Add Error Code.
- Update doc required of Tag API.
- Supported Coip.
- Add reeor code.
- Add ErrorCode.
- Increased errorCode NotSupportLinkrole for API ActivateRouterInterface.
- Fixed IncorrectStatus bug for APIs, ActivateRouterInterface, ConnectRouterInterface and DeactivateRouterInterface.
- Add new errorcode.
- Support source ip ram for GetVpcRouteEntrySummary.

2023-07-04 Version: 3.0.0
- Interface modification with parameter deletion is incompatible.
- Remove CreateNatIp remove useless parameter NatIpCidrId, must specify NatIpCidr.

2023-06-09 Version: 2.0.28
- RegionId Field is required.
- Supported Zone for AllocateEipSegmentAddress.
- Supported ReservationData for DescribeIpv6Addresses.
- Add ErrorCode.
- Supported ClientIp Ram check For AddPublicIpAddressPoolCidrBlock.
- Supported InstanceId and IpAddress For AllocateEipAddress.
- Support error code for the port range of SSL VPN server.
- Modify api timeout.
- Support Ha Vpn.
- Add error code.

2023-05-22 Version: 2.0.27
- Add ErrorCode.
- AssociateRouteTable and UnassociateRouteTable Supported Idempotence.
- Fix bugs for network acl region when query data.
- Fixed the field regionId of CreateNetworkAcl response.
- Supported new errorCode for AssociateEipAddressBatch.
- Update httpStatusCode for  Forbidden.
- Supported clientIP for PublicIpAddressPool.
- VPC and CommomBandwidth return tag info.
- Support coupon query price.
- Support auto renew router interface.
- Support accept-language.
- Add error code illegal resourceGroupId.
- Change the partial output reference visibility.

2023-05-03 Version: 2.0.26
- Supported Zone for AllocateEipAddress.
- Support HA-VPN.
- CreateFullNatEntry, ModifyFullNatEntryAttribute, DeleteFullNatEntry support idempotent.
- Support VBR allow prefixes.
- Support adDetailLocation.
- Fix ErrorCode.

2023-04-15 Version: 2.0.25
- CreateForwardEntry add error code.
- Fix description error.
- Add Error Code.
- Parameter Tag is requeired for TagResources.
- Add error code and message.
- Supported Zone for AllocateEipAddress.
- Add Delete IPv4Gw ErrorCode.
- Supported Ipam for Vpc.
- Support for multi-zone backend.
- Add ErrorCode.
- Add new ErrorCode and TrafficMirror supports to cumtomize PackageLength.

2023-03-28 Version: 2.0.24
- Support create pconn with tag.
- Add errorcode for OpenFlowLogService.
- Supported BandwidthPackageId for DescribeEipAddresses.
- The number oftraffic mirror source on the gateway side is limited to 30.
- Support associate transfer.
- Hide OrderId of AllocateEipSegmentAddress.
- Update error code of DeleteVSwitch.
- CreateFullNatEntry add error code.
- Support tag and resource group for dhcp options set and gateway endpoint.
- Fixed bugs for CreationTime.
- Fix pageNo.
- Add errorcode for AssociateEipAddress.
- Modify timeout.

2023-03-10 Version: 2.0.23
- Support create default VPC and create default vSwitch .

2023-03-07 Version: 2.0.22
- Add UnassociateNetworkAcl api error code.
- Add ram error code.
- Error code update.
- Add AdminQueryVpcInfo  control policy.
- OpenFlowLogService add errorcode.
- CreateNatIp add error code.
- Modify errorCode for OpenFlowLogService.
- Add  error code.
- Add errorCode for OpenFlowLogService.
- Delete access control policy.
- Add ControlPolicy for DescribeNatgates.
- Supported ControlPolicy For Natgw API.
- Fix TrafficPath Name.
- Add ForceDeleteVpc Param.

2023-02-18 Version: 2.0.21
- Eip error code update.
- Add CreateRouteEntry ErrorCode.
- Support batch operate route entries to 50.
- Fix TotalCount display error.
- Fixed bugs for DescribePublicIpAddress.
- Support error code.
- Support tag for traffic mirro and tag optimizes.
- Add new errorcode in ModifyVpnAttachmentAttribute CreateVpnAttachment, CreateVpnConnection.
- Havip support resource group and tag.
- FlowLog supports resource group and tag.
- Diagnose vpn connections history api release.
- Add error code for VpcDescribeVpcNatGatewayNetworkInterfaceQuota.
- Support  tag and resource group for traffic mirror and tag API optimized.
- VPN Tag.
- Add error code.
- Fix total field mapping.
- Supported delete pconn.
- Add Error Code.
- Support tag and resource group for sub resource of vpc.
- Supported BandwidthPackageId for DescribeEipAddresses.
- Update error code.
- BandwidthPackageId offline for DescribeEipAddresses.
- Update meta info of API.

2023-01-31 Version: 2.0.20
- Supported set high definition monitor log status for eip.
- Supported batch associate eip to cloud products.
- Supported VpcDescribeVpcNatGatewayNetworkInterfaceQuota.

2023-01-31 Version: 2.0.19
- Supported set high definition monitor log status for eip.
- Supported batch associate eip to cloud products.
- Supported VpcDescribeVpcNatGatewayNetworkInterfaceQuota.

2023-01-16 Version: 2.0.18
- Supported set high definition monitor log status for eip.
- Supported batch associate eip to cloud products.
- Supported VpcDescribeVpcNatGatewayNetworkInterfaceQuota.

2023-01-09 Version: 2.0.17
- Fix typos in ErrorCodes.
- Add ErrorMessage translation.
- Vpn support tag.
- Add attachment resource for terraform.
- Support diagnose vpn connection.
- Change timeout and api rate limit for fullnat.
- Add error Code.
- Add error code dependencyViolation vSwitchCidrReservation.
- Change input param.
- Add errorcode  IncorrectVpcStatus for action CreateVpnRouteEntry.
- Add errorcode FinancialLocked for action DeleteVpnConnection.
- Support resource group and tags.
- Support Return ResourceUid.

2022-12-22 Version: 2.0.16
- Supported set high definition monitor log status for eip.
- Supported batch associate eip to cloud products.

2022-12-22 Version: 2.0.15
- Support FlowLog Managed.
- Add error code for DeleteFullNatEntry, ListFullNatEntries, DescribeNatGateways.
- Change timeout for CreateFullNatEntry, DescribeNatGateways.
- Add error code.
- TagCode ExpressConnect.

2022-12-15 Version: 2.0.14
- Change DeleteFullNatEntry timeout.
- Add error code.
- Add error code for DeleteFullNatEntry.
- Fix error message.
- Fixed wrong char.

2022-12-09 Version: 2.0.13
- Add error code.
- Fix createVBR error message.
- Support vbrCrossCen grant.
- Fix bugs.
- Add new errorcode and error message in some API.
- Modify some error message in some error code.
- Modify parameter CustomerGatewayId in ModifyVpnAttachmentAttribute.

2022-11-21 Version: 2.0.12
- ResponseLog true.
- Support bandwidth.
- Fix error code translation error.
- Repair error code English translation.
- Changes the param NextToken of ListDhcpOptionsSet to optional in API docs.
- Fixed CreateVpcPrefixList paramer name invalid.

2022-11-14 Version: 2.0.11
- Supplementary error code mapping.
- Exposed unassociate ipv6 cidr param.
- Support Eip bind IpAddress.
- Supported query prefix list out add regionId.
- Support clearBgpAuthKey for ModifyBgpGroupAttribute.
- Add errorcode.
- CreateNatIpCidr natIpCidr must set.
- Fixed bugs for stsToken for DescribeEcGrantRelation.

2022-09-20 Version: 2.0.10
- DescribeSnatTableEntries DescribeSnatTableEntries ListFullnatEntries support query --by natGatewayId.

2022-09-01 Version: 2.0.9
- Support DescribeNatGateways return EipBindMode.

2022-08-31 Version: 2.0.8
- Support DescribeEipAddresses return Tags.

2022-08-26 Version: 2.0.7
- Support DescribeNatGateways return Tags.

2022-08-19 Version: 2.0.6
- Optimize DescribePublicIpAddress API.

2022-08-19 Version: 2.0.5
- Add DescribePublicIpAddress Interface.

2022-08-15 Version: 2.0.4
- Add param eipbindmode for api CreateNatGateway.

2022-08-02 Version: 2.0.3
- Supported latest apis.

2021-12-05 Version: 2.0.2
- Generated python 2016-04-28 for Vpc.

2021-12-02 Version: 2.0.1
- AMP Version Change.

2020-12-30 Version: 2.0.0
- AMP Version Change.

2020-09-02 Version: 1.0.1
- Generated python 2016-04-28 for Vpc.

