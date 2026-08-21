# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddVodStorageForAppRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        storage_location: str = None,
        storage_type: str = None,
    ):
        # The application ID. The application ID is the value of the `AppId` parameter returned by the [CreateAppInfo](~~CreateAppInfo~~) or [ListAppInfo](~~ListAppInfo~~) operation.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The OSS bucket address. This parameter is required when StorageType is set to user_oss_bucket.
        self.storage_location = storage_location
        # The storage type. Valid values:
        # 
        # - vod_oss_bucket
        # - user_oss_bucket
        # 
        # Default value: **vod_oss_bucket**.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

