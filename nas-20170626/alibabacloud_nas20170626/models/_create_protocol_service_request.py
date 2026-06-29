# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProtocolServiceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        protocol_spec: str = None,
        protocol_type: str = None,
        throughput: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may differ for each API request.
        self.client_token = client_token
        # The description of the protocol service. This value is displayed as "Protocol service name" in the console.
        # 
        # Limits:
        # 
        # - The description must be 2 to 128 characters in length.
        # - The description must start with a letter or Chinese character and cannot start with `http://` or `https://`.
        # - The description can contain digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # Specifies whether to perform a dry run for this request.
        # 
        # A dry run checks parameter validity and dependencies without actually creating the instance or incurring charges.
        # 
        # Valid values:
        # - true: Sends a check request without creating the protocol service. The check items include whether required parameters are specified, the request format, and business limit dependencies. If the check fails, the corresponding error is returned. If the check passes, HTTP status code 200 is returned, but ProtocolServiceId is empty.
        # - false (default): Sends a normal request. After the check passes, the instance is directly created.
        self.dry_run = dry_run
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The specification of the protocol service.
        # 
        # Valid values: General (default).
        # 
        # This parameter is required.
        self.protocol_spec = protocol_spec
        # The protocol type of the protocol service.
        # 
        # Valid values: NFS (default). Only NFSv3 access is supported.
        # 
        # This parameter is required.
        self.protocol_type = protocol_type
        # The bandwidth of the protocol service.
        # 
        # Unit: MB/s.
        self.throughput = throughput
        # The vSwitch ID of the protocol service.
        # 
        # If the storage redundancy type of the file system is zone-redundant storage (ZRS), do not set this parameter. Otherwise, this parameter is required.
        self.v_switch_id = v_switch_id
        # The VPC ID of the protocol service. The VPC must be the same as the VPC of the file system.
        # 
        # If the storage redundancy type of the file system is zone-redundant storage (ZRS), do not set this parameter. Otherwise, this parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.protocol_spec is not None:
            result['ProtocolSpec'] = self.protocol_spec

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.throughput is not None:
            result['Throughput'] = self.throughput

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('ProtocolSpec') is not None:
            self.protocol_spec = m.get('ProtocolSpec')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('Throughput') is not None:
            self.throughput = m.get('Throughput')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

