# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetStorageListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        storage_info_list: List[main_models.GetStorageListResponseBodyStorageInfoList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The storage configurations.
        self.storage_info_list = storage_info_list

    def validate(self):
        if self.storage_info_list:
            for v1 in self.storage_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StorageInfoList'] = []
        if self.storage_info_list is not None:
            for k1 in self.storage_info_list:
                result['StorageInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.storage_info_list = []
        if m.get('StorageInfoList') is not None:
            for k1 in m.get('StorageInfoList'):
                temp_model = main_models.GetStorageListResponseBodyStorageInfoList()
                self.storage_info_list.append(temp_model.from_map(k1))

        return self

class GetStorageListResponseBodyStorageInfoList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        creation_time: str = None,
        default_storage: bool = None,
        editing_temp_file_storage: bool = None,
        modified_time: str = None,
        path: str = None,
        status: str = None,
        storage_location: str = None,
        storage_type: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The time when the configuration was created.
        self.creation_time = creation_time
        # Indicates whether it is the default storage location.
        self.default_storage = default_storage
        # Indicates whether temporary files created during editing processes are stored in this location.
        self.editing_temp_file_storage = editing_temp_file_storage
        # The time when the configuration was last modified.
        self.modified_time = modified_time
        # The file path.
        self.path = path
        # The OSS storage status.
        self.status = status
        # The bucket.
        self.storage_location = storage_location
        # The storage type.
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

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.default_storage is not None:
            result['DefaultStorage'] = self.default_storage

        if self.editing_temp_file_storage is not None:
            result['EditingTempFileStorage'] = self.editing_temp_file_storage

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.path is not None:
            result['Path'] = self.path

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DefaultStorage') is not None:
            self.default_storage = m.get('DefaultStorage')

        if m.get('EditingTempFileStorage') is not None:
            self.editing_temp_file_storage = m.get('EditingTempFileStorage')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

