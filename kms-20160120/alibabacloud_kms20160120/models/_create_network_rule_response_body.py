# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNetworkRuleResponseBody(DaraModel):
    def __init__(
        self,
        arn: str = None,
        description: str = None,
        name: str = None,
        request_id: str = None,
        source_private_ip: str = None,
        type: str = None,
    ):
        # The ARN of the access control rule.
        self.arn = arn
        # The description.
        self.description = description
        # The name of the access control rule.
        self.name = name
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The private IP address or private CIDR block.
        self.source_private_ip = source_private_ip
        # The network type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_private_ip is not None:
            result['SourcePrivateIp'] = self.source_private_ip

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourcePrivateIp') is not None:
            self.source_private_ip = m.get('SourcePrivateIp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

