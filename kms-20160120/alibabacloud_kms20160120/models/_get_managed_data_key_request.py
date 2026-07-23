# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetManagedDataKeyRequest(DaraModel):
    def __init__(
        self,
        data_key_name: str = None,
        data_key_version_id: str = None,
        use_latest: bool = None,
    ):
        # The name of the managed data key (DK). This parameter is required.
        self.data_key_name = data_key_name
        # The version number of the managed data key (DK). This parameter is optional. If you set this parameter to a specific version number, the plaintext of the specified version of the managed data key (DK) is returned.
        self.data_key_version_id = data_key_version_id
        # Specifies whether to use the latest version of the managed data key (DK) when no version number is provided. Valid values:
        # 
        # - true: Returns the latest version of the managed data key (DK).
        # - false: Returns the first version of the managed data key (DK).
        # 
        # Default value: false.
        self.use_latest = use_latest

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_key_name is not None:
            result['DataKeyName'] = self.data_key_name

        if self.data_key_version_id is not None:
            result['DataKeyVersionId'] = self.data_key_version_id

        if self.use_latest is not None:
            result['UseLatest'] = self.use_latest

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataKeyName') is not None:
            self.data_key_name = m.get('DataKeyName')

        if m.get('DataKeyVersionId') is not None:
            self.data_key_version_id = m.get('DataKeyVersionId')

        if m.get('UseLatest') is not None:
            self.use_latest = m.get('UseLatest')

        return self

