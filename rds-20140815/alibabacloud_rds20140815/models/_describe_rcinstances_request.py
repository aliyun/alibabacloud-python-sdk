# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRCInstancesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        description: str = None,
        description_for_fuzzy: str = None,
        host_ip: str = None,
        image_id: str = None,
        instance_id: str = None,
        instance_ids: str = None,
        instance_name: str = None,
        page_number: int = None,
        page_size: int = None,
        public_ip: str = None,
        region_id: str = None,
        status: str = None,
        tag: str = None,
        vpc_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.description = description
        self.description_for_fuzzy = description_for_fuzzy
        # Queries instances by host IP address.
        self.host_ip = host_ip
        self.image_id = image_id
        # The instance ID. This parameter is used to query a single instance.
        # 
        # > If no instance ID is specified (neither **InstanceId** nor **InstanceIds** is passed), the operation returns detailed information about all RDS Custom instances in the specified region.
        self.instance_id = instance_id
        # The instance IDs.
        # 
        # This parameter is used to query multiple instances at a time. Separate multiple instance IDs with commas (,). A maximum of 100 IDs are supported. Input format: `["InstanceID1","InstanceID2"]`.
        # 
        # > If both **InstanceIds** and **InstanceId** are specified, the value of **InstanceIds** takes precedence.
        self.instance_ids = instance_ids
        # The instance name.
        self.instance_name = instance_name
        # The page number of the instance status list.
        # 
        # Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page for a paged query.
        # 
        # Maximum value: 100. Default value: 10.
        self.page_size = page_size
        # Queries instances by public IP address.
        self.public_ip = public_ip
        # The region ID. This parameter is required.
        self.region_id = region_id
        # The instance status. Valid values:
        # 
        # - **Pending**: Being created.
        # - **Running**: Running.
        # - **Starting**: Being started.
        # - **Stopping**: Being stopped.
        # - **Stopped**: Stopped.
        self.status = status
        # Queries instances by the specified tag. Input format: `{"TagKey":"TagValue"}`.
        self.tag = tag
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.description is not None:
            result['Description'] = self.description

        if self.description_for_fuzzy is not None:
            result['DescriptionForFuzzy'] = self.description_for_fuzzy

        if self.host_ip is not None:
            result['HostIp'] = self.host_ip

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DescriptionForFuzzy') is not None:
            self.description_for_fuzzy = m.get('DescriptionForFuzzy')

        if m.get('HostIp') is not None:
            self.host_ip = m.get('HostIp')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

