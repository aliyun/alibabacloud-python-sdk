# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListInstanceAdbAttributesRequest(DaraModel):
    def __init__(
        self,
        external_ip: str = None,
        instance_ids: List[str] = None,
        internal_ip: str = None,
        internal_port: str = None,
        ip_protocol: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The public IP address.
        self.external_ip = external_ip
        # The list of cloud phone instance IDs. You can specify from 1 to 100 IDs.
        self.instance_ids = instance_ids
        # The private IP address.
        self.internal_ip = internal_ip
        # The ADB port number.
        self.internal_port = internal_port
        # The network protocol type.
        self.ip_protocol = ip_protocol
        # The maximum number of records to return on each page for a paged query. Valid values: 1 to 100. Default value: 100.
        self.max_results = max_results
        # The token that indicates the position from which the query starts. If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip

        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')

        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

