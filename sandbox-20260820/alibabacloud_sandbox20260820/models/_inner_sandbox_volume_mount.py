# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class InnerSandboxVolumeMount(DaraModel):
    def __init__(
        self,
        agentic_fs: main_models.InnerSandboxVolumeMountAgenticFs = None,
        named: main_models.InnerSandboxVolumeMountNamed = None,
        oss: main_models.InnerSandboxVolumeMountOss = None,
    ):
        self.agentic_fs = agentic_fs
        self.named = named
        self.oss = oss

    def validate(self):
        if self.agentic_fs:
            self.agentic_fs.validate()
        if self.named:
            self.named.validate()
        if self.oss:
            self.oss.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agentic_fs is not None:
            result['agenticFs'] = self.agentic_fs.to_map()

        if self.named is not None:
            result['named'] = self.named.to_map()

        if self.oss is not None:
            result['oss'] = self.oss.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agenticFs') is not None:
            temp_model = main_models.InnerSandboxVolumeMountAgenticFs()
            self.agentic_fs = temp_model.from_map(m.get('agenticFs'))

        if m.get('named') is not None:
            temp_model = main_models.InnerSandboxVolumeMountNamed()
            self.named = temp_model.from_map(m.get('named'))

        if m.get('oss') is not None:
            temp_model = main_models.InnerSandboxVolumeMountOss()
            self.oss = temp_model.from_map(m.get('oss'))

        return self

class InnerSandboxVolumeMountOss(DaraModel):
    def __init__(
        self,
        mount_points: List[main_models.InnerSandboxVolumeMountOssMountPoints] = None,
    ):
        self.mount_points = mount_points

    def validate(self):
        if self.mount_points:
            for v1 in self.mount_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['mountPoints'] = []
        if self.mount_points is not None:
            for k1 in self.mount_points:
                result['mountPoints'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_points = []
        if m.get('mountPoints') is not None:
            for k1 in m.get('mountPoints'):
                temp_model = main_models.InnerSandboxVolumeMountOssMountPoints()
                self.mount_points.append(temp_model.from_map(k1))

        return self

class InnerSandboxVolumeMountOssMountPoints(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_path: str = None,
        endpoint: str = None,
        mount_dir: str = None,
        read_only: bool = None,
    ):
        self.bucket_name = bucket_name
        self.bucket_path = bucket_path
        self.endpoint = endpoint
        self.mount_dir = mount_dir
        self.read_only = read_only

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name

        if self.bucket_path is not None:
            result['bucketPath'] = self.bucket_path

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.mount_dir is not None:
            result['mountDir'] = self.mount_dir

        if self.read_only is not None:
            result['readOnly'] = self.read_only

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')

        if m.get('bucketPath') is not None:
            self.bucket_path = m.get('bucketPath')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('mountDir') is not None:
            self.mount_dir = m.get('mountDir')

        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')

        return self

class InnerSandboxVolumeMountNamed(DaraModel):
    def __init__(
        self,
        mount_points: List[main_models.InnerSandboxVolumeMountNamedMountPoints] = None,
    ):
        self.mount_points = mount_points

    def validate(self):
        if self.mount_points:
            for v1 in self.mount_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['mountPoints'] = []
        if self.mount_points is not None:
            for k1 in self.mount_points:
                result['mountPoints'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_points = []
        if m.get('mountPoints') is not None:
            for k1 in m.get('mountPoints'):
                temp_model = main_models.InnerSandboxVolumeMountNamedMountPoints()
                self.mount_points.append(temp_model.from_map(k1))

        return self

class InnerSandboxVolumeMountNamedMountPoints(DaraModel):
    def __init__(
        self,
        mount_dir: str = None,
        volume_name: str = None,
    ):
        self.mount_dir = mount_dir
        self.volume_name = volume_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_dir is not None:
            result['mountDir'] = self.mount_dir

        if self.volume_name is not None:
            result['volumeName'] = self.volume_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mountDir') is not None:
            self.mount_dir = m.get('mountDir')

        if m.get('volumeName') is not None:
            self.volume_name = m.get('volumeName')

        return self

class InnerSandboxVolumeMountAgenticFs(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        mount_points: List[main_models.InnerSandboxVolumeMountAgenticFsMountPoints] = None,
        user_id: int = None,
    ):
        self.group_id = group_id
        self.mount_points = mount_points
        self.user_id = user_id

    def validate(self):
        if self.mount_points:
            for v1 in self.mount_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['groupID'] = self.group_id

        result['mountPoints'] = []
        if self.mount_points is not None:
            for k1 in self.mount_points:
                result['mountPoints'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['userID'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupID') is not None:
            self.group_id = m.get('groupID')

        self.mount_points = []
        if m.get('mountPoints') is not None:
            for k1 in m.get('mountPoints'):
                temp_model = main_models.InnerSandboxVolumeMountAgenticFsMountPoints()
                self.mount_points.append(temp_model.from_map(k1))

        if m.get('userID') is not None:
            self.user_id = m.get('userID')

        return self

class InnerSandboxVolumeMountAgenticFsMountPoints(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        agentic_space_id: str = None,
        file_system_id: str = None,
        mount_dir: str = None,
        server_addr: str = None,
    ):
        self.access_point_id = access_point_id
        self.agentic_space_id = agentic_space_id
        self.file_system_id = file_system_id
        self.mount_dir = mount_dir
        self.server_addr = server_addr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['accessPointID'] = self.access_point_id

        if self.agentic_space_id is not None:
            result['agenticSpaceID'] = self.agentic_space_id

        if self.file_system_id is not None:
            result['fileSystemID'] = self.file_system_id

        if self.mount_dir is not None:
            result['mountDir'] = self.mount_dir

        if self.server_addr is not None:
            result['serverAddr'] = self.server_addr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessPointID') is not None:
            self.access_point_id = m.get('accessPointID')

        if m.get('agenticSpaceID') is not None:
            self.agentic_space_id = m.get('agenticSpaceID')

        if m.get('fileSystemID') is not None:
            self.file_system_id = m.get('fileSystemID')

        if m.get('mountDir') is not None:
            self.mount_dir = m.get('mountDir')

        if m.get('serverAddr') is not None:
            self.server_addr = m.get('serverAddr')

        return self

