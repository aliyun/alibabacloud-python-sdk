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
        # Base64-encoded public key content.
        # 
        # This parameter is required.
        self.content = content
        # Description of the public key.
        self.description = description
        # Group for the public key. Used for public key management.
        # 
        # 1. Length: 0 to 255 characters.
        # 
        # 2. Valid characters: lowercase letters, digits, underscores (_), hyphens (-), and periods (.).
        # 
        # 3. First character must be a letter or digit.
        self.key_group = key_group
        # Name of the public key. Must be unique.
        # 
        # 1. Length: 8 to 255 characters.
        # 
        # 2. Valid characters: lowercase letters, digits, underscores (_), hyphens (-), and periods (.).
        # 
        # 3. First character must be a letter or digit.
        # 
        # 4. Prefix cannot be group-.
        # 
        # This parameter is required.
        self.key_name = key_name
        # Type of the public key. Valid values:
        # 
        # - **adb**: ADB key.
        # 
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

