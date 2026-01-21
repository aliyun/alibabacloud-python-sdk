# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListHostShareKeysResponseBody(DaraModel):
    def __init__(
        self,
        host_share_keys: List[main_models.ListHostShareKeysResponseBodyHostShareKeys] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the shared keys.
        self.host_share_keys = host_share_keys
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of the shared keys.
        self.total_count = total_count

    def validate(self):
        if self.host_share_keys:
            for v1 in self.host_share_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HostShareKeys'] = []
        if self.host_share_keys is not None:
            for k1 in self.host_share_keys:
                result['HostShareKeys'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_share_keys = []
        if m.get('HostShareKeys') is not None:
            for k1 in m.get('HostShareKeys'):
                temp_model = main_models.ListHostShareKeysResponseBodyHostShareKeys()
                self.host_share_keys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListHostShareKeysResponseBodyHostShareKeys(DaraModel):
    def __init__(
        self,
        host_account_count: int = None,
        host_share_key_id: str = None,
        host_share_key_name: str = None,
        last_modify_key_at: int = None,
        private_key_finger_print: str = None,
    ):
        # The number of the associated host accounts.
        self.host_account_count = host_account_count
        # The shared key ID.
        self.host_share_key_id = host_share_key_id
        # The name of the shared key.
        self.host_share_key_name = host_share_key_name
        # The time when the shared key was last modified. The value is a UNIX timestamp. Unit: seconds.
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
        if self.host_account_count is not None:
            result['HostAccountCount'] = self.host_account_count

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
        if m.get('HostAccountCount') is not None:
            self.host_account_count = m.get('HostAccountCount')

        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')

        if m.get('HostShareKeyName') is not None:
            self.host_share_key_name = m.get('HostShareKeyName')

        if m.get('LastModifyKeyAt') is not None:
            self.last_modify_key_at = m.get('LastModifyKeyAt')

        if m.get('PrivateKeyFingerPrint') is not None:
            self.private_key_finger_print = m.get('PrivateKeyFingerPrint')

        return self

