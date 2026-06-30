# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AssociateAclsWithListenerRequest(DaraModel):
    def __init__(
        self,
        acl_ids: List[str] = None,
        acl_type: str = None,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        # The ID of the access control policy group. You can associate up to two access control policy groups.
        # 
        # This parameter is required.
        self.acl_ids = acl_ids
        # The type of access control. Valid values:
        # - **white**: Only requests from the IP addresses or CIDR blocks Settings in the specified access control policy group are forwarded. Whitelists are applicable to scenarios in which you want to allow only specific IP addresses to access your application. After you enable a whitelist, only the IP addresses in the whitelist can access the Global Accelerator listener. If you enable a whitelist but the access control policy group does not contain any IP addresses, the Global Accelerator listener forwards all requests.
        # - **black**: All requests from the IP addresses or CIDR blocks Settings in the specified access control policy group are blocked. Blacklists are applicable to scenarios in which you want to block specific IP addresses from accessing your application. If you enable a blacklist but the access control policy group does not contain any IP addresses, the Global Accelerator listener forwards all requests.
        # 
        # This parameter is required.
        self.acl_type = acl_type
        # The client token that is used to ensure the idempotency of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** value as the **ClientToken** value. The **RequestId** value is different for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # - **true**: performs a dry run without associating the resources. The system checks the required parameters, request syntax, and business limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # - **false** (default): performs a dry run and sends the request. If the request passes the dry run, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The listener ID.
        # 
        # Only intelligent routing listeners support the access control feature.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The region ID of the Global Accelerator instance. Set the value to **ap-southeast-1**.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids

        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')

        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

