# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVpcPeerConnectionRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        enable_jumbo_frame: bool = None,
        instance_id: str = None,
        link_type: str = None,
        name: str = None,
    ):
        # The new bandwidth of the VPC peering connection. Unit: Mbit/s. The value must be an integer greater than 0.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that the value is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # The new description of the VPC peering connection.
        # 
        # The description must be 1 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to perform a dry run. Valid values:
        # - **true**: performs a dry run without modifying the information. The system checks whether required parameters are specified, the request format is valid, and service limits are met. If the request fails the check, an error is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        # - **false** (default): sends a normal request. If the request passes the check, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # Specifies whether the jumbo frame feature is enabled for the VPC peering connection. Valid values:
        # - true: enabled.
        # - false: disabled.
        # > Note: To specify this parameter, make sure that you create a cross-region peering connection.
        self.enable_jumbo_frame = enable_jumbo_frame
        # The instance ID of the VPC peering connection whose name or description you want to modify.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The link type.
        # 
        # Valid values: Platinum and Gold. Default value: Gold.
        # 
        # > To specify this parameter, make sure that you create a cross-region peering connection.
        self.link_type = link_type
        # The new name of the VPC peering connection.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.enable_jumbo_frame is not None:
            result['EnableJumboFrame'] = self.enable_jumbo_frame

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.link_type is not None:
            result['LinkType'] = self.link_type

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EnableJumboFrame') is not None:
            self.enable_jumbo_frame = m.get('EnableJumboFrame')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LinkType') is not None:
            self.link_type = m.get('LinkType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

