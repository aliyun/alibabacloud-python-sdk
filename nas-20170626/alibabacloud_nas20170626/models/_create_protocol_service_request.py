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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The description of the protocol service. The name of the protocol service appears in the console.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter and cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # Specifies whether to perform a dry run.
        # 
        # The dry run checks parameter validity and prerequisites. The dry run does not create a protocol service or incur fees.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run and does not create the protocol service. The system checks the request format, service limits, prerequisites, and whether the required parameters are specified. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the ProtocolServiceId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a protocol service is created.
        self.dry_run = dry_run
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The specification of the protocol service.
        # 
        # Set the value to General (default).
        # 
        # Valid values:
        # 
        # *   CL2
        # *   General
        # *   CL1
        # 
        # This parameter is required.
        self.protocol_spec = protocol_spec
        # The protocol type of the protocol service.
        # 
        # Valid value: NFS (default). Only NFSv3 is supported.
        # 
        # This parameter is required.
        self.protocol_type = protocol_type
        # The throughput of the protocol service.
        # 
        # Unit: MB/s.
        self.throughput = throughput
        # The vSwitch ID of the protocol service.
        self.v_switch_id = v_switch_id
        # The virtual private cloud (VPC) ID of the protocol service. The VPC ID of the protocol service must be the same as the VPC ID of the file system.
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

