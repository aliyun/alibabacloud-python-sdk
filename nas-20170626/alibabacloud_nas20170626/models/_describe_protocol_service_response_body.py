# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeProtocolServiceResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        protocol_services: List[main_models.DescribeProtocolServiceResponseBodyProtocolServices] = None,
        request_id: str = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The information about protocol services.
        self.protocol_services = protocol_services
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.protocol_services:
            for v1 in self.protocol_services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['ProtocolServices'] = []
        if self.protocol_services is not None:
            for k1 in self.protocol_services:
                result['ProtocolServices'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.protocol_services = []
        if m.get('ProtocolServices') is not None:
            for k1 in m.get('ProtocolServices'):
                temp_model = main_models.DescribeProtocolServiceResponseBodyProtocolServices()
                self.protocol_services.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeProtocolServiceResponseBodyProtocolServices(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        file_system_id: str = None,
        instance_base_throughput: int = None,
        instance_burst_throughput: int = None,
        instance_ram: int = None,
        modify_time: str = None,
        mount_target_count: int = None,
        protocol_service_id: str = None,
        protocol_spec: str = None,
        protocol_throughput: int = None,
        protocol_type: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The time when the protocol service was created. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the protocol service.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter and cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The base throughput of the protocol service. Unit: MB/s.
        self.instance_base_throughput = instance_base_throughput
        # The burst throughput of the protocol service. Unit: MB/s.
        self.instance_burst_throughput = instance_burst_throughput
        # The memory cache size of the protocol service. Unit: GiB.
        self.instance_ram = instance_ram
        # The time when the protocol service was modified. The time is displayed in UTC.
        self.modify_time = modify_time
        # The total number of CPFS directories and filesets exported in the protocol service.
        self.mount_target_count = mount_target_count
        # The ID of the protocol service.
        self.protocol_service_id = protocol_service_id
        # The specification of the protocol service.
        # 
        # *   Valid value: General.
        # *   Default value: General.
        self.protocol_spec = protocol_spec
        # The throughput of the protocol service. Unit: MB/s.
        self.protocol_throughput = protocol_throughput
        # The protocol type supported by the protocol service.
        # 
        # Valid values:
        # 
        # *   NFS: The protocol service supports access over the Network File System (NFS) protocol.
        self.protocol_type = protocol_type
        # The status of the protocol service.
        # 
        # Valid values:
        # 
        # *   Creating: The protocol service is being created.
        # *   Starting: The protocol service is being started.
        # *   Running: The protocol service is running.
        # *   Updating: The protocol service is being updated.
        # *   Deleting: The protocol service is being deleted.
        # *   Stopping: The protocol service is being stopped.
        # *   Stopped: The protocol service is stopped.
        self.status = status
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.instance_base_throughput is not None:
            result['InstanceBaseThroughput'] = self.instance_base_throughput

        if self.instance_burst_throughput is not None:
            result['InstanceBurstThroughput'] = self.instance_burst_throughput

        if self.instance_ram is not None:
            result['InstanceRAM'] = self.instance_ram

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.mount_target_count is not None:
            result['MountTargetCount'] = self.mount_target_count

        if self.protocol_service_id is not None:
            result['ProtocolServiceId'] = self.protocol_service_id

        if self.protocol_spec is not None:
            result['ProtocolSpec'] = self.protocol_spec

        if self.protocol_throughput is not None:
            result['ProtocolThroughput'] = self.protocol_throughput

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('InstanceBaseThroughput') is not None:
            self.instance_base_throughput = m.get('InstanceBaseThroughput')

        if m.get('InstanceBurstThroughput') is not None:
            self.instance_burst_throughput = m.get('InstanceBurstThroughput')

        if m.get('InstanceRAM') is not None:
            self.instance_ram = m.get('InstanceRAM')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('MountTargetCount') is not None:
            self.mount_target_count = m.get('MountTargetCount')

        if m.get('ProtocolServiceId') is not None:
            self.protocol_service_id = m.get('ProtocolServiceId')

        if m.get('ProtocolSpec') is not None:
            self.protocol_spec = m.get('ProtocolSpec')

        if m.get('ProtocolThroughput') is not None:
            self.protocol_throughput = m.get('ProtocolThroughput')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

