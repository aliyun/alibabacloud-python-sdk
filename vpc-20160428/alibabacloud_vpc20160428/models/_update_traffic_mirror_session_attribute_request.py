# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTrafficMirrorSessionAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        enabled: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        packet_length: int = None,
        priority: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        traffic_mirror_filter_id: str = None,
        traffic_mirror_session_description: str = None,
        traffic_mirror_session_id: str = None,
        traffic_mirror_session_name: str = None,
        traffic_mirror_target_id: str = None,
        traffic_mirror_target_type: str = None,
        virtual_network_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run, without performing the actual request. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**: sends the request. If the request passes the check, a 2xx HTTP status code is returned and the operation is performed. This is the default value.
        self.dry_run = dry_run
        # Specifies whether to enable the traffic mirror session. Valid values:
        # 
        # *   **false** (default)
        # *   **true**
        self.enabled = enabled
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The maximum transmission unit (MTU).
        # 
        # Valid values: **64 to 9600**. Default value: **1500**.
        self.packet_length = packet_length
        # The new priority of the traffic mirror session. Valid values: **1** to **32766**.
        # 
        # A smaller value indicates a higher priority. You cannot specify identical priorities for traffic mirror sessions that are created in the same region by using the same account.
        self.priority = priority
        # The region ID of the traffic mirror session. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list. For more information about the regions that support traffic mirror, see [Overview of traffic mirror](https://help.aliyun.com/document_detail/207513.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the traffic mirror filter.
        self.traffic_mirror_filter_id = traffic_mirror_filter_id
        # The new description of the traffic mirror session.
        # 
        # The description must be 1 to 256 characters in length and cannot start with `http://` or `https://`.
        self.traffic_mirror_session_description = traffic_mirror_session_description
        # The ID of the traffic mirror session.
        # 
        # This parameter is required.
        self.traffic_mirror_session_id = traffic_mirror_session_id
        # The new name of the traffic mirror session.
        # 
        # The name must be 1 to 128 characters in length, and cannot start with `http://` or `https://`.
        self.traffic_mirror_session_name = traffic_mirror_session_name
        # The ID of the traffic mirror destination.
        self.traffic_mirror_target_id = traffic_mirror_target_id
        # The new type of the traffic mirror destination. Valid values:
        # 
        # *   **NetworkInterface**: an elastic network interface (ENI)
        # *   **SLB**: an internal-facing Server Load Balancer (SLB) instance
        self.traffic_mirror_target_type = traffic_mirror_target_type
        # The VXLAN network identifier (VNI) that is used to distinguish different mirrored traffic. Valid values: **0** to **16777215**.
        # 
        # You can use VNIs to identify mirrored traffic from different sessions at the traffic mirror destination. If you do not specify a VNI, the system randomly allocates a VNI. If you want the system to randomly allocate a VNI, ignore this parameter.
        self.virtual_network_id = virtual_network_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.packet_length is not None:
            result['PacketLength'] = self.packet_length

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.traffic_mirror_filter_id is not None:
            result['TrafficMirrorFilterId'] = self.traffic_mirror_filter_id

        if self.traffic_mirror_session_description is not None:
            result['TrafficMirrorSessionDescription'] = self.traffic_mirror_session_description

        if self.traffic_mirror_session_id is not None:
            result['TrafficMirrorSessionId'] = self.traffic_mirror_session_id

        if self.traffic_mirror_session_name is not None:
            result['TrafficMirrorSessionName'] = self.traffic_mirror_session_name

        if self.traffic_mirror_target_id is not None:
            result['TrafficMirrorTargetId'] = self.traffic_mirror_target_id

        if self.traffic_mirror_target_type is not None:
            result['TrafficMirrorTargetType'] = self.traffic_mirror_target_type

        if self.virtual_network_id is not None:
            result['VirtualNetworkId'] = self.virtual_network_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PacketLength') is not None:
            self.packet_length = m.get('PacketLength')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TrafficMirrorFilterId') is not None:
            self.traffic_mirror_filter_id = m.get('TrafficMirrorFilterId')

        if m.get('TrafficMirrorSessionDescription') is not None:
            self.traffic_mirror_session_description = m.get('TrafficMirrorSessionDescription')

        if m.get('TrafficMirrorSessionId') is not None:
            self.traffic_mirror_session_id = m.get('TrafficMirrorSessionId')

        if m.get('TrafficMirrorSessionName') is not None:
            self.traffic_mirror_session_name = m.get('TrafficMirrorSessionName')

        if m.get('TrafficMirrorTargetId') is not None:
            self.traffic_mirror_target_id = m.get('TrafficMirrorTargetId')

        if m.get('TrafficMirrorTargetType') is not None:
            self.traffic_mirror_target_type = m.get('TrafficMirrorTargetType')

        if m.get('VirtualNetworkId') is not None:
            self.virtual_network_id = m.get('VirtualNetworkId')

        return self

