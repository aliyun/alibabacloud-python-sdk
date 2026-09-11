# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class CreateCpfsAccessPointRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        file_system_id: str = None,
        region_id: str = None,
        root_directory: main_models.CreateCpfsAccessPointRequestRootDirectory = None,
        tag: List[main_models.CreateCpfsAccessPointRequestTag] = None,
    ):
        # The description of the access point.
        # 
        # Limits:
        # - The description must be 2 to 128 characters in length.
        # - The description must start with a letter.
        # - The description cannot start with http:// or https://.
        # - The description can contain digits, colons (:), underscores (_), or hyphens (-).
        self.description = description
        # The file system ID.
        # 
        # - Cloud Parallel File Storage (CPFS): must start with `cpfs-`, such as cpfs-125487\\*\\*\\*\\*.
        # 
        # - CPFS for Lingjun: must start with `bmcpfs-`, such as bmcpfs-0015\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The root directory of the access point. Default value: "/".
        self.root_directory = root_directory
        # The list of tags for the CPFS access point.
        self.tag = tag

    def validate(self):
        if self.root_directory:
            self.root_directory.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.root_directory is not None:
            result['RootDirectory'] = self.root_directory.to_map()

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RootDirectory') is not None:
            temp_model = main_models.CreateCpfsAccessPointRequestRootDirectory()
            self.root_directory = temp_model.from_map(m.get('RootDirectory'))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateCpfsAccessPointRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateCpfsAccessPointRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateCpfsAccessPointRequestRootDirectory(DaraModel):
    def __init__(
        self,
        root_path: str = None,
    ):
        # The root directory of the access point. The value must start and end with a forward slash (/).
        self.root_path = root_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.root_path is not None:
            result['RootPath'] = self.root_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RootPath') is not None:
            self.root_path = m.get('RootPath')

        return self

