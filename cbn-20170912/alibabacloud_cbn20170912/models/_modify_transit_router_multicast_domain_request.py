# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ModifyTransitRouterMulticastDomainRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        options: main_models.ModifyTransitRouterMulticastDomainRequestOptions = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        transit_router_multicast_domain_description: str = None,
        transit_router_multicast_domain_id: str = None,
        transit_router_multicast_domain_name: str = None,
    ):
        # A client token that ensures the idempotence of the request.
        # 
        # Generate a unique token on your client for each request. The token can contain only ASCII characters.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: Performs a dry run. The system checks the required parameters, request format, and service limits. If the check fails, an error message is returned. If the check passes, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): Sends the request. If the request passes the check, the name and description of the multicast domain are modified.
        self.dry_run = dry_run
        # The feature options of the multicast domain.
        self.options = options
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The new description of the multicast domain.
        # 
        # The description can be empty or 1 to 256 characters long. It cannot start with http\\:// or https\\://.
        self.transit_router_multicast_domain_description = transit_router_multicast_domain_description
        # The ID of the multicast domain.
        # 
        # This parameter is required.
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id
        # The new name of the multicast domain.
        # 
        # The name can be empty or 1 to 128 characters long. It cannot start with http\\:// or https\\://.
        self.transit_router_multicast_domain_name = transit_router_multicast_domain_name

    def validate(self):
        if self.options:
            self.options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.transit_router_multicast_domain_description is not None:
            result['TransitRouterMulticastDomainDescription'] = self.transit_router_multicast_domain_description

        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id

        if self.transit_router_multicast_domain_name is not None:
            result['TransitRouterMulticastDomainName'] = self.transit_router_multicast_domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Options') is not None:
            temp_model = main_models.ModifyTransitRouterMulticastDomainRequestOptions()
            self.options = temp_model.from_map(m.get('Options'))

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TransitRouterMulticastDomainDescription') is not None:
            self.transit_router_multicast_domain_description = m.get('TransitRouterMulticastDomainDescription')

        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')

        if m.get('TransitRouterMulticastDomainName') is not None:
            self.transit_router_multicast_domain_name = m.get('TransitRouterMulticastDomainName')

        return self

class ModifyTransitRouterMulticastDomainRequestOptions(DaraModel):
    def __init__(
        self,
        igmpv_2support: str = None,
        strict_source_control: str = None,
    ):
        # Specifies whether to enable the Internet Group Management Protocol (IGMP) feature for the multicast domain. When this feature is enabled, hosts can use IGMP to dynamically join or leave multicast groups. Set the value to **enable**.
        # 
        # > - The IGMP feature is in public preview. To use this feature, contact your account manager.
        # >
        # > - You cannot disable the IGMP feature after it is enabled.
        self.igmpv_2support = igmpv_2support
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

