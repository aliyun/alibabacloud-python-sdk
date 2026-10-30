# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveIpRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        ip_list: str = None,
        region_id: str = None,
        source_instance_id: str = None,
    ):
        # The ID of the destination Anti-DDoS Origin instance.
        # 
        # > You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances.
        self.instance_id = instance_id
        # The list of IP addresses to migrate to an Anti-DDoS Origin instance for protection. The list is represented as a character string in JSON array format. Each element in the JSON array is a structure that contains the following fields:
        # 
        # - **ip**: String type. Required. The IP address to add.
        # 
        # - **member_uid**: String type. Optional. The member accounts to which the asset belongs. This field is required only when you add an asset under member accounts. Example: [{"ip":"121.41.XX.XX","member_uid":"120100811162****"}]
        self.ip_list = ip_list
        # The region ID of the Anti-DDoS Origin instance.
        # 
        # > You can call the DescribeRegions operation to query all regions supported by Anti-DDoS Origin.
        self.region_id = region_id
        # The ID of the source Anti-DDoS Origin instance.
        # 
        # > You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances.
        self.source_instance_id = source_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip_list is not None:
            result['IpList'] = self.ip_list

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')

        return self

