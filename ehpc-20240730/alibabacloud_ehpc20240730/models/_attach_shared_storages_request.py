# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class AttachSharedStoragesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        shared_storages: List[main_models.AttachSharedStoragesRequestSharedStorages] = None,
    ):
        # The cluster ID.
        # 
        # You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The information about the shared storage resources that you want to attach to the cluster.
        # 
        # This parameter is required.
        self.shared_storages = shared_storages

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
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        result['SharedStorages'] = []
        if self.shared_storages is not None:
            for k1 in self.shared_storages:
                result['SharedStorages'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        self.shared_storages = []
        if m.get('SharedStorages') is not None:
            for k1 in m.get('SharedStorages'):
                temp_model = main_models.AttachSharedStoragesRequestSharedStorages()
                self.shared_storages.append(temp_model.from_map(k1))

        return self

class AttachSharedStoragesRequestSharedStorages(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        location: str = None,
        mount_directory: str = None,
        mount_options: str = None,
        mount_target: str = None,
        protocol_type: str = None,
        storage_directory: str = None,
        volume_type: str = None,
    ):
        # The ID of the file system to be attached.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The storage location of the file system to be attached. Valid values:
        # 
        # *   OnPremise: The file system is deployed on a hybrid cloud.
        # *   PublicCloud: The file system is deployed on a public cloud.
        self.location = location
        # The local mount directory of the file system that you want to attach.
        # 
        # This parameter is required.
        self.mount_directory = mount_directory
        # The attaching options of the file system to be attached. Valid values:
        # 
        # *   \\-t nfs -o vers=3,nolock,proto=tcp,noresvport
        # *   \\-t nfs -o vers=4.0,noresvport
        # 
        # Default value:-t nfs -o vers=3,nolock,proto=tcp,noresvport
        # 
        # >  The v3 version is recommended for higher performance if multiple Elastic Compute Service (ECS) instances do not edit the same file at the same time.
        self.mount_options = mount_options
        # The address of the mount point of the file system to be attached.
        # 
        # This parameter is required.
        self.mount_target = mount_target
        # The protocol type of the file system to be attached. Valid values:
        # 
        # *   NFS
        # *   SMB
        # 
        # This parameter is required.
        self.protocol_type = protocol_type
        # The storage directory of the file system. You can mount any directory in the file system to the specified cluster directory.
        # 
        # This parameter is required.
        self.storage_directory = storage_directory
        # The type of the file system to be attached. Valid values:
        # 
        # *   nas
        # *   cpfs
        # 
        # This parameter is required.
        self.volume_type = volume_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.location is not None:
            result['Location'] = self.location

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

        if self.volume_type is not None:
            result['VolumeType'] = self.volume_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('Location') is not None:
            self.location = m.get('Location')

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

        if m.get('VolumeType') is not None:
            self.volume_type = m.get('VolumeType')

        return self

