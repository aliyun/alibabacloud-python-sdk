# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePrivateNetworkWhiteIpsRequest(DaraModel):
    def __init__(
        self,
        body: str = None,
        client_token: str = None,
        modify_mode: str = None,
    ):
        # The VPC private network access whitelist or whitelist group configuration of the instance.
        self.body = body
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The modification method. Valid values:
        # 
        # - Cover (default): overwrites the original IP address whitelist with the value of the ips parameter.
        # 
        # - Append: adds the IP addresses specified by the ips parameter to the original IP address whitelist.
        # 
        # - Delete: deletes the IP addresses specified by the ips parameter from the original IP address whitelist. You must retain at least one IP address.
        self.modify_mode = modify_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.modify_mode is not None:
            result['modifyMode'] = self.modify_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('modifyMode') is not None:
            self.modify_mode = m.get('modifyMode')

        return self

