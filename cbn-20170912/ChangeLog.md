2023-10-21 Version: 1.0.35
- Generated python 2017-09-12 for Cbn.

2023-09-12 Version: 1.0.34
- Generated python 2017-09-12 for Cbn.

2023-09-08 Version: 1.0.33
- Generated python 2017-09-12 for Cbn.

2023-08-08 Version: 1.0.32
- Generated python 2017-09-12 for Cbn.

2023-08-08 Version: 1.0.31
- Generated python 2017-09-12 for Cbn.

2023-07-13 Version: 1.0.30
- Update API ListTransitRouterRouteEntries to support PathAttributes.

2023-05-23 Version: 1.0.29
- Update API DescribeGrantRulesToCen support ChildInstanceOwnerId and ChildInstanceId.

2023-04-27 Version: 1.0.28
- Update API DescribeCenAttachedChildInstanceAttribute support returning VPC Cidrs.

2023-03-17 Version: 1.0.27
- Update API CreateTransitRouteTableAggregation update request parameter TransitRouteTableAggregationScop to TransitRouteTableAggregationScope.
- Update API DescribeTransitRouteTableAggregation update response parameter Scop to Scope.

2023-03-13 Version: 1.0.26
- Update API DescribeCens support parameter resourceGroupId.
- Update API DescribeCens support parameter resourceGroupId, tag and response resourceGroupId, tags.

2023-01-13 Version: 1.0.25
- New API CreateTransitRouteTableAggregation.
- New API DeleteTransitRouteTableAggregation.
- New API DescribeTransitRouteTableAggregation.
- New API DescribeTransitRouteTableAggregationDetail.
- New API RefreshTransitRouteTableAggregation.
- Update API CreateTransitRouterRouteTable support parameter RouteTableOptions.
- Update API UpdateTransitRouterRouteTable support parameter RouteTableOptions.
- Update API ListTransitRouterRouteTables support parameter RouteTableOptions and response RegionId, RouteTableOptions.
- Update API UpdateTrafficMarkingPolicyAttribute support parameter AddTrafficMatchRules and DeleteTrafficMatchRules.
- Update API ListTransitRouters support parameter Status, Type, TransitRouterName and FeatureFilter.
- Update API DescribeFlowlogs support response TransitRouterAttachmentId and Interval.
- Update API ListTransitRouterVpcAttachments support parameter OrderType, Status and response OrderType.
- Update API ListTransitRouterRouteTableAssociations support parameter TransitRouterAttachmentResourceId, TransitRouterAttachmentResourceType and Status.
- Update API ListTransitRouterRouteTablePropagations support parameter TransitRouterAttachmentResourceId, TransitRouterAttachmentResourceType and Status.

2022-12-08 Version: 1.0.24
- Add ListCenChildInstanceRouteEntriesToAttachment support query VPC instance route to Vpc Attachment.
- Add ListTransitRouterAttachmentPropagations support query TransitRouter Propagations by Attachment Id.
- ListTransitRouterMulticastGroups: add parameter isGroupSource, isGroupMember and NetworkInterfaceIds. add response TransitRouterMulticastDomainId. 
- ListMulticastDomains: add response TransitRouterId.
- ListCenInterRegionTrafficQosPolicies: add response TransitRouterId and TransitRouterAttachmentId. 
- ListTrafficMarkingPolicies: add response TransitRouterId.
- DescribeFlowlogs: add parameter TransitRouterAttachmentId.
- DeleteTransitRouterConnectPeer: add ErrorCode.
- ListTransitRouterVpcAttachments: add parameter VpcId.
- ListTransitRouterMulticastGroups: param TransitRouterMulticastDomainId Required False.
- DeleteTransitRouterConnectAttachment: add parameter Force.
- DeleteTransitRouterVpcAttachment : add parameter Force.
- DeleteTransitRouterVpnAttachment : add parameter Force.
- DeleteTransitRouterVbrAttachment : add parameter Force.

2022-11-28 Version: 1.0.23
- Add CreateTransitRouterCidr support create TR Cidr.
- Add ModifyTransitRouterCidr support modify TR Cidr.
- Add DeleteTransitRouterCidr support delete TR Cidr.
- Add ListTransitRouterCidr support list TR Cidr.
- Add ListTransitRouterCidrAllocation support list TR Cidr allocation.
- Update CreateTransitRouter support TR Cidr list.
- Update ListTransitRouters support Cidr list.
- Update ListTransitRouterVpnAttachments response support ChargeType.
- CreateFlowlog add parameter tag.
- DescribeFlowlogs add parameter tag and add response tags.
- CreateTransitRouterMulticastDomain add parameter tag.
- ListTransitRouterMulticastDomains add parameter tag and add response tags.
- CreateTransitRouterRouteTable add parameter tag.
- ListTransitRouterRouteTables add parameter tag and add response tags.
- CreateTransitRouter add parameter tag.
- ListTransitRouters add parameter tag and add response tags.

2022-11-22 Version: 1.0.22
- Update ListTransitRouterMulticastGroups offline parameter ConnectPeerId.
- Update CreateCenBandwidthPackage offline parameter ServiceType.
- Update ModifyCenBandwidthPackageSpec offline parameter ServiceType.
- Update DescribeCenBandwidthPackages offline parameter ServiceType.

2022-11-02 Version: 1.0.21
- Update ListTransitRouterPrefixListAssociation support NextHop and NextHopType filter.
- Update ListTransitRouterPrefixListAssociation support TransitRouterRouteTableId  filter.
- Update ListTrafficMarkingPolicies no TrafficMatchRules field in response if no TrafficMarkingPolicyId in request.
- Update ListCenInterRegionTrafficQosPolicies no TrafficQosQueues field in response if no TrafficQosPolicyId in request.

2022-09-23 Version: 1.0.20
- Add new API DescribeGrantRulesToResource .
- Update DescribeGrantRulesToCen support MaxResult and nextToken .
- Update ListTransitRouterPrefixlistAssociation return TransitRouterId and TransitRouterTableId .

2022-08-26 Version: 1.0.19
- Update param NextHopType visibility for DeleteTransitRouterPrefixListAssociation .

2022-08-26 Version: 1.0.18
- Add AvailableZones for ListTransitRouterAvailableResource.

2022-04-27 Version: 1.0.17
- update to latest.

2022-04-15 Version: 1.0.16
- Support Multicast.
- RouteMap Support sub-table.

2022-03-10 Version: 1.0.15
- Modify the input parameter Action of CreateCen to be required.

2022-01-11 Version: 1.0.14
- Support  DeleteTransitRouter API.

2021-12-21 Version: 1.0.13
- Support Darabonba API.

2021-05-06 Version: 1.0.2
- Generated python 2017-09-12 for Cbn.

2021-04-23 Version: 1.0.1
- Generated python 2017-09-12 for Cbn.

2020-12-29 Version: 1.0.0
- AMP Version Change.

