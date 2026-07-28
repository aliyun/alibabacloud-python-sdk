# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateTrafficMirrorSessionRequest(DaraModel):
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
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreateTrafficMirrorSessionRequestTag] = None,
        traffic_mirror_filter_id: str = None,
        traffic_mirror_session_description: str = None,
        traffic_mirror_session_name: str = None,
        traffic_mirror_source_ids: List[str] = None,
        traffic_mirror_target_id: str = None,
        traffic_mirror_target_type: str = None,
        virtual_network_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): performs a dry run and sends the request. If the request passes the dry run, the traffic mirror session is created.
        self.dry_run = dry_run
        # Specifies whether to enable the traffic mirror session. Valid values:
        # 
        # - **false** (default): does not enable the traffic mirror session.
        # 
        # - **true**: enables the traffic mirror session.
        self.enabled = enabled
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The maximum length of the mirrored original packet, excluding the VXLAN packet length. Default value: **1500**. Valid values: **64** to **8500**. Unit: bytes.
        # - This parameter affects the length of packets received at the traffic mirror destination. For more information, see the mirrored packet length and MTU limits in [Traffic mirroring overview](https://help.aliyun.com/document_detail/207513.html).
        # 
        # - This parameter is available only in specific regions. For more information, see the description of the mirrored packet length parameter in [Create and manage traffic mirrors](https://help.aliyun.com/document_detail/207514.html).
        self.packet_length = packet_length
        # The priority of traffic mirror session. Valid values: **1** to **32766**.
        # A smaller value indicates a higher priority. The priorities of traffic mirror sessions created in the same region under the same account must be unique.
        # 
        # This parameter is required.
        self.priority = priority
        # The region ID of the traffic mirror session. You can call [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) to query the most recent region list. For information about the regions that support traffic mirroring, see [Traffic mirroring overview](https://help.aliyun.com/document_detail/207513.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the traffic mirroring instance belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags of the resource.
        self.tag = tag
        # The instance ID of the traffic mirror filter.
        # 
        # This parameter is required.
        self.traffic_mirror_filter_id = traffic_mirror_filter_id
        # The description of the traffic mirror session.
        # 
        # The description must be 1 to 256 characters in length and cannot start with `http://` or `https://`.
        self.traffic_mirror_session_description = traffic_mirror_session_description
        # The name of the traffic mirror session.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.traffic_mirror_session_name = traffic_mirror_session_name
        # The instance ID of the traffic mirror source. Elastic network interfaces (ENIs) are supported as traffic mirror sources. The default value of **N** is **1**, which indicates that only one traffic mirror source can be added to a traffic mirror session.
        # 
        # This parameter is required.
        self.traffic_mirror_source_ids = traffic_mirror_source_ids
        # The instance ID of the traffic mirror destination. Elastic network interfaces (ENIs) and private network load balancing instances are supported as traffic mirror destinations.
        # 
        # This parameter is required.
        self.traffic_mirror_target_id = traffic_mirror_target_id
        # The type of the traffic mirror destination. Valid values:
        # 
        # - **NetworkInterface**: elastic network interface (ENI).
        # 
        # - **SLB**: private network load balancing instance.
        # 
        # This parameter is required.
        self.traffic_mirror_target_type = traffic_mirror_target_type
        # The VXLAN network identifier (VNI) that is used to distinguish mirrored data from different traffic mirror sessions. Valid values: **0** to **16777215**.
        # 
        # You can use the VNI to identify mirrored data from different sessions at the traffic mirror destination. You can specify a custom VNI or use a system-assigned value. To use a system-assigned value, do not specify this parameter. The system randomly allocates the value.
        self.virtual_network_id = virtual_network_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.traffic_mirror_filter_id is not None:
            result['TrafficMirrorFilterId'] = self.traffic_mirror_filter_id

        if self.traffic_mirror_session_description is not None:
            result['TrafficMirrorSessionDescription'] = self.traffic_mirror_session_description

        if self.traffic_mirror_session_name is not None:
            result['TrafficMirrorSessionName'] = self.traffic_mirror_session_name

        if self.traffic_mirror_source_ids is not None:
            result['TrafficMirrorSourceIds'] = self.traffic_mirror_source_ids

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateTrafficMirrorSessionRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TrafficMirrorFilterId') is not None:
            self.traffic_mirror_filter_id = m.get('TrafficMirrorFilterId')

        if m.get('TrafficMirrorSessionDescription') is not None:
            self.traffic_mirror_session_description = m.get('TrafficMirrorSessionDescription')

        if m.get('TrafficMirrorSessionName') is not None:
            self.traffic_mirror_session_name = m.get('TrafficMirrorSessionName')

        if m.get('TrafficMirrorSourceIds') is not None:
            self.traffic_mirror_source_ids = m.get('TrafficMirrorSourceIds')

        if m.get('TrafficMirrorTargetId') is not None:
            self.traffic_mirror_target_id = m.get('TrafficMirrorTargetId')

        if m.get('TrafficMirrorTargetType') is not None:
            self.traffic_mirror_target_type = m.get('TrafficMirrorTargetType')

        if m.get('VirtualNetworkId') is not None:
            self.virtual_network_id = m.get('VirtualNetworkId')

        return self

class CreateTrafficMirrorSessionRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
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

