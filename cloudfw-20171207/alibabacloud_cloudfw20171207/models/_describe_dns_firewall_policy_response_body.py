# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeDnsFirewallPolicyResponseBody(DaraModel):
    def __init__(
        self,
        page_no: str = None,
        page_size: str = None,
        policys: List[main_models.DescribeDnsFirewallPolicyResponseBodyPolicys] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The DNS firewall access control policies.
        self.policys = policys
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.policys:
            for v1 in self.policys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Policys'] = []
        if self.policys is not None:
            for k1 in self.policys:
                result['Policys'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.policys = []
        if m.get('Policys') is not None:
            for k1 in m.get('Policys'):
                temp_model = main_models.DescribeDnsFirewallPolicyResponseBodyPolicys()
                self.policys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDnsFirewallPolicyResponseBodyPolicys(DaraModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
        description: str = None,
        destination: str = None,
        destination_addrs: List[str] = None,
        destination_group_type: str = None,
        destination_type: str = None,
        direction: str = None,
        hit_last_time: int = None,
        hit_times: int = None,
        ip_version: int = None,
        priority: int = None,
        release: str = None,
        source: str = None,
        source_addrs: List[str] = None,
        source_group_type: str = None,
        source_type: str = None,
    ):
        # The action that is performed on traffic that matches the access control policy. Valid values:
        # 
        # - **accept**: allows the traffic.
        # 
        # - **drop**: denies the traffic.
        # 
        # - **log**: monitors the traffic.
        self.acl_action = acl_action
        # The unique ID of the access control policy.
        self.acl_uuid = acl_uuid
        # The description of the access control policy.
        self.description = description
        # The destination address in the access control policy. Valid values:
        # 
        # - If **DestinationType** is `net`, the value of this parameter is a destination CIDR block.
        # 
        # - If **DestinationType** is `domain`, the value of this parameter is a destination domain.
        # 
        # - If **DestinationType** is `group`, the value of this parameter is the name of a destination address book.
        self.destination = destination
        # The destination addresses in the address book.
        self.destination_addrs = destination_addrs
        # The type of the destination address book in the access control policy. Valid values:
        # 
        # - **ip**: an IP address book
        # 
        # - **domain**: a domain address book
        self.destination_group_type = destination_group_type
        # The type of the destination address in the access control policy. Valid values:
        # 
        # - **net**: destination CIDR block
        # 
        # - **group**: destination address book
        # 
        # - **domain**: destination domain
        # 
        # - **location**: destination location
        self.destination_type = destination_type
        # The direction of the traffic to which the access control policy applies. Valid values:
        # 
        # - **in**: inbound traffic
        # 
        # - **out**: outbound traffic
        self.direction = direction
        # The last time the policy was hit. The value is a UNIX timestamp. Unit: seconds.
        self.hit_last_time = hit_last_time
        # The number of hits for the access control policy.
        self.hit_times = hit_times
        # The IP version supported by the access control policy. Valid values:
        # 
        # - **4**: IPv4
        # 
        # - **6**: IPv6
        self.ip_version = ip_version
        # The priority of the access control policy. A smaller value indicates a higher priority.
        self.priority = priority
        # Indicates whether the access control policy is enabled. After a policy is created, it is enabled by default. Valid values:
        # 
        # - **true**: enabled
        # 
        # - **false**: disabled
        self.release = release
        # The source address in the access control policy. Valid values:
        # 
        # - If **SourceType** is `net`, the value of this parameter is a source CIDR block. Example: 192.0.XX.XX/24.
        # 
        # - If **SourceType** is `group`, the value of this parameter is the name of a source address book. Example: db_group.
        # 
        # - If **SourceType** is `location`, the value of this parameter is a location. For more information about the valid values of this parameter, see [AddControlPolicy](https://help.aliyun.com/document_detail/138867.html). Example: ["BJ11", "ZB"].
        self.source = source
        # The source addresses.
        self.source_addrs = source_addrs
        # The type of the source address book in the access control policy. Valid values:
        # 
        # - **ip**: an IP address book
        # 
        # - **tag**: a tag address book
        # 
        # - **domain**: a domain address book
        # 
        # - **threat**: a threat intelligence address book
        # 
        # - **backsrc**: a back-to-origin address book
        self.source_group_type = source_group_type
        # The type of the source address in the access control policy. Valid values:
        # 
        # - **net**: a source CIDR block
        # 
        # - **group**: a source address book
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action

        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid

        if self.description is not None:
            result['Description'] = self.description

        if self.destination is not None:
            result['Destination'] = self.destination

        if self.destination_addrs is not None:
            result['DestinationAddrs'] = self.destination_addrs

        if self.destination_group_type is not None:
            result['DestinationGroupType'] = self.destination_group_type

        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.hit_last_time is not None:
            result['HitLastTime'] = self.hit_last_time

        if self.hit_times is not None:
            result['HitTimes'] = self.hit_times

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.release is not None:
            result['Release'] = self.release

        if self.source is not None:
            result['Source'] = self.source

        if self.source_addrs is not None:
            result['SourceAddrs'] = self.source_addrs

        if self.source_group_type is not None:
            result['SourceGroupType'] = self.source_group_type

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')

        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Destination') is not None:
            self.destination = m.get('Destination')

        if m.get('DestinationAddrs') is not None:
            self.destination_addrs = m.get('DestinationAddrs')

        if m.get('DestinationGroupType') is not None:
            self.destination_group_type = m.get('DestinationGroupType')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('HitLastTime') is not None:
            self.hit_last_time = m.get('HitLastTime')

        if m.get('HitTimes') is not None:
            self.hit_times = m.get('HitTimes')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Release') is not None:
            self.release = m.get('Release')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceAddrs') is not None:
            self.source_addrs = m.get('SourceAddrs')

        if m.get('SourceGroupType') is not None:
            self.source_group_type = m.get('SourceGroupType')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

