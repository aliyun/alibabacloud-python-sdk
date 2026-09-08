# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class CreateTransitRouterMulticastDomainRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        options: main_models.CreateTransitRouterMulticastDomainRequestOptions = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreateTransitRouterMulticastDomainRequestTag] = None,
        transit_router_id: str = None,
        transit_router_multicast_domain_description: str = None,
        transit_router_multicast_domain_name: str = None,
    ):
        # The instance ID of the Cloud Enterprise Network (CEN).
        self.cen_id = cen_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # - **false** (default): performs a dry run and sends the request. If the request passes the dry run, the multicast domain is created.
        self.dry_run = dry_run
        # The multicast domain feature options.
        self.options = options
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the transit router instance.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag information.
        # 
        # You can specify up to 20 tags at a time.
        self.tag = tag
        # The instance ID of the transit router.
        self.transit_router_id = transit_router_id
        # The description of the multicast domain.
        # 
        # The description can be empty or 1 to 256 characters in length, and cannot start with http:// or https://.
        self.transit_router_multicast_domain_description = transit_router_multicast_domain_description
        # The name of the multicast domain.
        # 
        # The name can be empty or 1 to 128 characters in length, and cannot start with http:// or https://.
        self.transit_router_multicast_domain_name = transit_router_multicast_domain_name

    def validate(self):
        if self.options:
            self.options.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.options is not None:
            result['Options'] = self.options.to_map()

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.transit_router_multicast_domain_description is not None:
            result['TransitRouterMulticastDomainDescription'] = self.transit_router_multicast_domain_description

        if self.transit_router_multicast_domain_name is not None:
            result['TransitRouterMulticastDomainName'] = self.transit_router_multicast_domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Options') is not None:
            temp_model = main_models.CreateTransitRouterMulticastDomainRequestOptions()
            self.options = temp_model.from_map(m.get('Options'))

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateTransitRouterMulticastDomainRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterMulticastDomainDescription') is not None:
            self.transit_router_multicast_domain_description = m.get('TransitRouterMulticastDomainDescription')

        if m.get('TransitRouterMulticastDomainName') is not None:
            self.transit_router_multicast_domain_name = m.get('TransitRouterMulticastDomainName')

        return self

class CreateTransitRouterMulticastDomainRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource.
        # 
        # Once you specify this parameter, it cannot be an empty string. The tag key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # You can specify up to 20 tag keys at a time.
        self.key = key
        # The tag value of the resource.
        # 
        # Once you specify this parameter, it cannot be empty. The tag value can be up to 128 characters in length and cannot start with aliyun or acs:. It cannot contain http:// or https://.
        # 
        # Each tag key corresponds to one tag value. You can specify up to 20 tag values at a time.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateTransitRouterMulticastDomainRequestOptions(DaraModel):
    def __init__(
        self,
        igmpv_2support: str = None,
        strict_source_control: str = None,
    ):
        # Specifies whether to enable the Internet Group Management Protocol (IGMP) feature for the multicast domain. After this feature is enabled, hosts can dynamically join or leave multicast groups by using the IGMP protocol. Valid values:
        # 
        # - **enable**: enables the IGMP feature.
        # - **disable** (default): disables the IGMP feature.
        # 
        # > - The IGMP feature is in public preview. To use this feature, contact your account manager to apply for permissions.
        # > - After the IGMP feature is enabled, it cannot be disabled.
        self.igmpv_2support = igmpv_2support
        # Specifies whether to enable the strict multicast source control feature. If this feature is disabled, all ECS instances in the associated vSwitch can serve as multicast sources. If this feature is enabled, only ENIs that are statically configured or that have sent IGMP Join messages can serve as multicast sources. Valid values:
        # 
        # - ``enable``: enables the strict multicast source control feature.
        # - ``disable``: disables the strict multicast source control feature.
        # 
        # > - The strict multicast source control feature takes effect only for multicast domains with the IGMP feature enabled.
        # > - Currently, only one multicast domain with the strict multicast source control feature disabled can be created under a transit router.
        self.strict_source_control = strict_source_control

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.igmpv_2support is not None:
            result['Igmpv2Support'] = self.igmpv_2support

        if self.strict_source_control is not None:
            result['StrictSourceControl'] = self.strict_source_control

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Igmpv2Support') is not None:
            self.igmpv_2support = m.get('Igmpv2Support')

        if m.get('StrictSourceControl') is not None:
            self.strict_source_control = m.get('StrictSourceControl')

        return self

