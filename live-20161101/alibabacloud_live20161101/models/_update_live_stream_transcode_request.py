# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLiveStreamTranscodeRequest(DaraModel):
    def __init__(
        self,
        app: str = None,
        domain: str = None,
        encrypt_parameters: str = None,
        lazy: str = None,
        owner_id: int = None,
        region_id: str = None,
        template: str = None,
    ):
        # The AppName of the live stream. This parameter cannot be modified.
        # 
        # This parameter is required.
        self.app = app
        # The streaming domain. This parameter cannot be modified.
        # 
        # This parameter is required.
        self.domain = domain
        # The encryption settings, formatted as a JSON string.
        # 
        # - **EncryptType**: The encryption type. Set the value to aliyun.
        # 
        # - **KmsKeyID**: The ID of the customer master key (CMK) in Key Management Service (KMS).
        # 
        # - **KmsKeyExpireInterval**: The key rotation period. Unit: seconds. Valid values: **60 to 3600.**
        # 
        # > When you use Digital Rights Management (DRM) encryption, you cannot modify **KmsKeyID**.
        self.encrypt_parameters = encrypt_parameters
        # Specifies whether to enable on-demand transcoding. Valid values:
        # 
        # - **yes**: Transcoding only starts when the first viewer requests this transcoded stream.
        # 
        # - **no**: Transcoding starts immediately after the stream is published.
        self.lazy = lazy
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The transcoding template name. This parameter cannot be modified.
        # 
        # This parameter is required.
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.encrypt_parameters is not None:
            result['EncryptParameters'] = self.encrypt_parameters

        if self.lazy is not None:
            result['Lazy'] = self.lazy

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.template is not None:
            result['Template'] = self.template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EncryptParameters') is not None:
            self.encrypt_parameters = m.get('EncryptParameters')

        if m.get('Lazy') is not None:
            self.lazy = m.get('Lazy')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        return self

