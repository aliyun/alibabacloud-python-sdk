# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class DetachSharedStoragesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        shared_storages: List[main_models.DetachSharedStoragesRequestSharedStorages] = None,
    ):
        # The cluster ID.
        # 
        # You can call the [ListClusters](https://help.aliyun.com/document_detail/87116.html) operation to query the cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The information about mounted shared storage resources.
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
                temp_model = main_models.DetachSharedStoragesRequestSharedStorages()
                self.shared_storages.append(temp_model.from_map(k1))

        return self

class DetachSharedStoragesRequestSharedStorages(DaraModel):
    def __init__(
        self,
        mount_directory: str = None,
    ):
        # The local mount directory of the mounted file system.
        # 
        # This parameter is required.
        self.mount_directory = mount_directory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_directory is not None:
            result['MountDirectory'] = self.mount_directory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountDirectory') is not None:
            self.mount_directory = m.get('MountDirectory')

        return self

