# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateTrustedOriginRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        trust_origin_name: str = None,
        trusted_origin_id: str = None,
        trusted_origin_scene: List[str] = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The ID of the IDaaS EIAM instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # If this parameter is not specified, the trusted origin name is not modified.
        self.trust_origin_name = trust_origin_name
        # The ID of the trusted origin.
        # 
        # This parameter is required.
        self.trusted_origin_id = trusted_origin_id
        # When specified, the existing values are entirely replaced. Only iframe_embed and cors are supported.
        self.trusted_origin_scene = trusted_origin_scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.trust_origin_name is not None:
            result['TrustOriginName'] = self.trust_origin_name

        if self.trusted_origin_id is not None:
            result['TrustedOriginId'] = self.trusted_origin_id

        if self.trusted_origin_scene is not None:
            result['TrustedOriginScene'] = self.trusted_origin_scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TrustOriginName') is not None:
            self.trust_origin_name = m.get('TrustOriginName')

        if m.get('TrustedOriginId') is not None:
            self.trusted_origin_id = m.get('TrustedOriginId')

        if m.get('TrustedOriginScene') is not None:
            self.trusted_origin_scene = m.get('TrustedOriginScene')

        return self

