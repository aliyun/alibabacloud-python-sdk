# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateTrustedOriginRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        origin: str = None,
        trust_origin_name: str = None,
        trusted_origin_scene: List[str] = None,
    ):
        # Ensures the idempotence of the request. Generate a value on your client and make sure that the value is unique across different requests. The ClientToken parameter supports only ASCII characters and can be up to 64 characters in length.
        self.client_token = client_token
        # The ID of the IDaaS EIAM instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The browser origin in the format of scheme://host[:port]. It cannot be modified after creation.
        # 
        # This parameter is required.
        self.origin = origin
        # The name of the trusted origin used for management, display, and auditing. If you do not specify this parameter, it is left empty.
        self.trust_origin_name = trust_origin_name
        # The trusted origin scenarios. Only iframe_embed and cors are supported. Specify at least one value.
        # 
        # This parameter is required.
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

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.trust_origin_name is not None:
            result['TrustOriginName'] = self.trust_origin_name

        if self.trusted_origin_scene is not None:
            result['TrustedOriginScene'] = self.trusted_origin_scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('TrustOriginName') is not None:
            self.trust_origin_name = m.get('TrustOriginName')

        if m.get('TrustedOriginScene') is not None:
            self.trusted_origin_scene = m.get('TrustedOriginScene')

        return self

