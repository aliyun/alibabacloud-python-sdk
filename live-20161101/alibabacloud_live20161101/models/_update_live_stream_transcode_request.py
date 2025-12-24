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
        # The name of the application to which the stream belongs, and it cannot be modified.
        # 
        # This parameter is required.
        self.app = app
        # Streamer domain name, not modifiable.
        # 
        # This parameter is required.
        self.domain = domain
        # The encryption configuration. The value is a JSON string. The following fields are included in the syntax:
        # 
        # *   EncryptType: the type of the encryption. Set the value to **aliyun**.
        # *   KmsKeyID: the ID of the CMK in KMS.
        # *   KmsKeyExpireInterval: the validity period of the CMK. Valid values: **60 to 3600**. Unit: seconds.
        self.encrypt_parameters = encrypt_parameters
        # Specifies whether to enable triggered transcoding. Valid values:
        # 
        # *   **yes**: enables triggered transcoding.
        # *   **no**: disables triggered transcoding.
        self.lazy = lazy
        self.owner_id = owner_id
        self.region_id = region_id
        # Transcoding template, not modifiable.
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

