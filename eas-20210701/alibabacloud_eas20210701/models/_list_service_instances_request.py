# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServiceInstancesRequest(DaraModel):
    def __init__(
        self,
        filter: str = None,
        host_ip: str = None,
        instance_ip: str = None,
        instance_name: str = None,
        instance_status: str = None,
        instance_type: str = None,
        is_spot: bool = None,
        list_replica: bool = None,
        member_type: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        quota_id: str = None,
        replica_name: str = None,
        resource: str = None,
        resource_type: str = None,
        role: str = None,
        sort: str = None,
    ):
        # The keyword used to query instances. Instances can be queried based on instance name, instance IP address, IP address of the server where the instance resides, and instance type.
        self.filter = filter
        # The IP address of the server where the instance resides.
        self.host_ip = host_ip
        # The IP address of the instance.
        self.instance_ip = instance_ip
        # The instance name.
        self.instance_name = instance_name
        # The instance state.
        self.instance_status = instance_status
        # The instance type.
        self.instance_type = instance_type
        # Specifies whether the instance is a preemptible instance.
        self.is_spot = is_spot
        self.list_replica = list_replica
        self.member_type = member_type
        # The sorting order.
        # 
        # Valid values:
        # 
        # *   asc
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     The instances are sorted in ascending order.
        # 
        # *   desc
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     The instances are sorted in descending order.
        self.order = order
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 100.
        self.page_size = page_size
        self.quota_id = quota_id
        self.replica_name = replica_name
        self.resource = resource
        # The type of the resource group to which the instance belongs.
        # 
        # Valid values:
        # 
        # *   PublicResource
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DedicatedResource
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.resource_type = resource_type
        # The service role.
        # 
        # Valid values:
        # 
        # *   DataSet
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     dataset service
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   SDProxy
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Stable-Diffusion proxy service
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Standard
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     standard service
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Queue
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     queue service
        # 
        #     <!-- -->
        # 
        #     .
        self.role = role
        # The field that you use to sort the query results.
        # 
        # *   Set the value to StartTime.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     The value specifies that the query results are sorted based on the time when the instances were created
        # 
        #     <!-- -->
        # 
        #     .
        self.sort = sort

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['Filter'] = self.filter

        if self.host_ip is not None:
            result['HostIP'] = self.host_ip

        if self.instance_ip is not None:
            result['InstanceIP'] = self.instance_ip

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.is_spot is not None:
            result['IsSpot'] = self.is_spot

        if self.list_replica is not None:
            result['ListReplica'] = self.list_replica

        if self.member_type is not None:
            result['MemberType'] = self.member_type

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.replica_name is not None:
            result['ReplicaName'] = self.replica_name

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.role is not None:
            result['Role'] = self.role

        if self.sort is not None:
            result['Sort'] = self.sort

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('HostIP') is not None:
            self.host_ip = m.get('HostIP')

        if m.get('InstanceIP') is not None:
            self.instance_ip = m.get('InstanceIP')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IsSpot') is not None:
            self.is_spot = m.get('IsSpot')

        if m.get('ListReplica') is not None:
            self.list_replica = m.get('ListReplica')

        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('ReplicaName') is not None:
            self.replica_name = m.get('ReplicaName')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        return self

