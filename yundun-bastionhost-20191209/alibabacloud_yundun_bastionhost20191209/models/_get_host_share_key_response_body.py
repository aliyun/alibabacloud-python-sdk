# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class GetHostShareKeyResponseBody(DaraModel):
    def __init__(
        self,
        host_share_key: main_models.GetHostShareKeyResponseBodyHostShareKey = None,
        request_id: str = None,
    ):
        # The returned information about the shared key.
        self.host_share_key = host_share_key
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.host_share_key:
            self.host_share_key.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_share_key is not None:
            result['HostShareKey'] = self.host_share_key.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostShareKey') is not None:
            temp_model = main_models.GetHostShareKeyResponseBodyHostShareKey()
            self.host_share_key = temp_model.from_map(m.get('HostShareKey'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetHostShareKeyResponseBodyHostShareKey(DaraModel):
    def __init__(
        self,
        host_share_key_id: str = None,
        host_share_key_name: str = None,
        last_modify_key_at: int = None,
        private_key_finger_print: str = None,
    ):
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id
        # The name of the shared key.
        self.host_share_key_name = host_share_key_name
        # The time when the information about the shared key was last modified. The value is a UNIX timestamp. Unit: seconds.
        self.last_modify_key_at = last_modify_key_at
        # The fingerprint of the private key.
        self.private_key_finger_print = private_key_finger_print

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id

        if self.host_share_key_name is not None:
            result['HostShareKeyName'] = self.host_share_key_name

        if self.last_modify_key_at is not None:
            result['LastModifyKeyAt'] = self.last_modify_key_at

        if self.private_key_finger_print is not None:
            result['PrivateKeyFingerPrint'] = self.private_key_finger_print

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')

        if m.get('HostShareKeyName') is not None:
            self.host_share_key_name = m.get('HostShareKeyName')

        if m.get('LastModifyKeyAt') is not None:
            self.last_modify_key_at = m.get('LastModifyKeyAt')

        if m.get('PrivateKeyFingerPrint') is not None:
            self.private_key_finger_print = m.get('PrivateKeyFingerPrint')

        return self

