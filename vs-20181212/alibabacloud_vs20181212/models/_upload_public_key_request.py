# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadPublicKeyRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        description: str = None,
        key_group: str = None,
        key_name: str = None,
        key_type: str = None,
    ):
        # The encoded content of the public key. The default encoding format is Base64.
        # 
        # This parameter is required.
        self.content = content
        # The description of the public key.
        self.description = description
        # The group of the public key. Used for public key management.
        # Naming conventions:
        # 1. The length must be 0 to 255 characters.
        # 2. The name can contain lowercase letters, digits, underscores (_), hyphens (-), and periods (.).
        # 3. The first character must be a letter or a digit.
        self.key_group = key_group
        # The name of the public key. The name must be unique.
        # Naming conventions:
        # 1. The length must be 8 to 255 characters.
        # 2. The name can contain lowercase letters, digits, underscores (_), hyphens (-), and periods (.).
        # 3. The first character must be a letter or a digit.
        # 4. The prefix cannot be "group-".
        # 
        # This parameter is required.
        self.key_name = key_name
        # The type of the public key. Valid values:
        # 
        # - **adb**: ADB key.
        # - **ssh**: SSH key.
        self.key_type = key_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.description is not None:
            result['Description'] = self.description

        if self.key_group is not None:
            result['KeyGroup'] = self.key_group

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.key_type is not None:
            result['KeyType'] = self.key_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('KeyGroup') is not None:
            self.key_group = m.get('KeyGroup')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')

        return self

