# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListUserPublicKeysResponseBody(DaraModel):
    def __init__(
        self,
        public_keys: List[main_models.ListUserPublicKeysResponseBodyPublicKeys] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the public keys of the user.
        self.public_keys = public_keys
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of public keys.
        self.total_count = total_count

    def validate(self):
        if self.public_keys:
            for v1 in self.public_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PublicKeys'] = []
        if self.public_keys is not None:
            for k1 in self.public_keys:
                result['PublicKeys'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.public_keys = []
        if m.get('PublicKeys') is not None:
            for k1 in m.get('PublicKeys'):
                temp_model = main_models.ListUserPublicKeysResponseBodyPublicKeys()
                self.public_keys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListUserPublicKeysResponseBodyPublicKeys(DaraModel):
    def __init__(
        self,
        comment: str = None,
        finger_print: str = None,
        public_key_id: str = None,
        public_key_name: str = None,
        user_id: str = None,
    ):
        # The description of the public key.
        self.comment = comment
        # The fingerprint of the public key.
        self.finger_print = finger_print
        # The ID of the public key.
        self.public_key_id = public_key_id
        # The name of the public key.
        self.public_key_name = public_key_name
        # The ID of the user to which the public key belongs.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.finger_print is not None:
            result['FingerPrint'] = self.finger_print

        if self.public_key_id is not None:
            result['PublicKeyId'] = self.public_key_id

        if self.public_key_name is not None:
            result['PublicKeyName'] = self.public_key_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('FingerPrint') is not None:
            self.finger_print = m.get('FingerPrint')

        if m.get('PublicKeyId') is not None:
            self.public_key_id = m.get('PublicKeyId')

        if m.get('PublicKeyName') is not None:
            self.public_key_name = m.get('PublicKeyName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

