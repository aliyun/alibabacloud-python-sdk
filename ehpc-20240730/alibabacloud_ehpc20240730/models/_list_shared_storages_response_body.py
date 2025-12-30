# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class ListSharedStoragesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        shared_storages: List[main_models.ListSharedStoragesResponseBodySharedStorages] = None,
        success: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the attached shared storage.
        self.shared_storages = shared_storages
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.shared_storages:
            for v1 in self.shared_storages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SharedStorages'] = []
        if self.shared_storages is not None:
            for k1 in self.shared_storages:
                result['SharedStorages'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.shared_storages = []
        if m.get('SharedStorages') is not None:
            for k1 in m.get('SharedStorages'):
                temp_model = main_models.ListSharedStoragesResponseBodySharedStorages()
                self.shared_storages.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListSharedStoragesResponseBodySharedStorages(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        file_system_protocol: str = None,
        file_system_type: str = None,
        mount_info: List[main_models.ListSharedStoragesResponseBodySharedStoragesMountInfo] = None,
    ):
        # The ID of the attached file system.
        self.file_system_id = file_system_id
        # The protocol used by the attached file system. Valid values:
        # 
        # *   nfs3
        # *   nfs4
        # *   cpfs
        self.file_system_protocol = file_system_protocol
        # The type of the attached file system. Valid values:
        # 
        # *   nas
        # *   cpfs
        self.file_system_type = file_system_type
        # The mount information.
        self.mount_info = mount_info

    def validate(self):
        if self.mount_info:
            for v1 in self.mount_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.file_system_protocol is not None:
            result['FileSystemProtocol'] = self.file_system_protocol

        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        result['MountInfo'] = []
        if self.mount_info is not None:
            for k1 in self.mount_info:
                result['MountInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FileSystemProtocol') is not None:
            self.file_system_protocol = m.get('FileSystemProtocol')

        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        self.mount_info = []
        if m.get('MountInfo') is not None:
            for k1 in m.get('MountInfo'):
                temp_model = main_models.ListSharedStoragesResponseBodySharedStoragesMountInfo()
                self.mount_info.append(temp_model.from_map(k1))

        return self

class ListSharedStoragesResponseBodySharedStoragesMountInfo(DaraModel):
    def __init__(
        self,
        mount_directory: str = None,
        mount_options: str = None,
        mount_target: str = None,
        protocol_type: str = None,
        storage_directory: str = None,
    ):
        # The local mount directory of the attached file system.
        self.mount_directory = mount_directory
        # The mount options for the attached file system. Valid values:
        # 
        # *   \\-t nfs -o vers=3,nolock,proto=tcp,noresvport
        # *   \\-t nfs -o vers=4.0,noresvport
        self.mount_options = mount_options
        # The mount target of the attached file system.
        self.mount_target = mount_target
        # The protocol used by the mount target of the attached file system. Valid values:
        # 
        # *   nfs3
        # *   nfs4
        # *   cpfs
        self.protocol_type = protocol_type
        # The storage directory of the attached file system.
        self.storage_directory = storage_directory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_directory is not None:
            result['MountDirectory'] = self.mount_directory

        if self.mount_options is not None:
            result['MountOptions'] = self.mount_options

        if self.mount_target is not None:
            result['MountTarget'] = self.mount_target

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.storage_directory is not None:
            result['StorageDirectory'] = self.storage_directory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountDirectory') is not None:
            self.mount_directory = m.get('MountDirectory')

        if m.get('MountOptions') is not None:
            self.mount_options = m.get('MountOptions')

        if m.get('MountTarget') is not None:
            self.mount_target = m.get('MountTarget')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('StorageDirectory') is not None:
            self.storage_directory = m.get('StorageDirectory')

        return self

