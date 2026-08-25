# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class ListDirectoriesResponseBody(DaraModel):
    def __init__(
        self,
        directories: List[main_models.ListDirectoriesResponseBodyDirectories] = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        # The directories.
        self.directories = directories
        # The request ID.
        self.request_id = request_id
        # The number of directories.
        self.total_counts = total_counts

    def validate(self):
        if self.directories:
            for v1 in self.directories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Directories'] = []
        if self.directories is not None:
            for k1 in self.directories:
                result['Directories'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.directories = []
        if m.get('Directories') is not None:
            for k1 in m.get('Directories'):
                temp_model = main_models.ListDirectoriesResponseBodyDirectories()
                self.directories.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')

        return self

class ListDirectoriesResponseBodyDirectories(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        directory_id: str = None,
        directory_name: str = None,
        region: str = None,
        update_time: str = None,
    ):
        # The time when the directory was created.
        self.create_time = create_time
        # The ID of the directory.
        self.directory_id = directory_id
        # The name of the directory.
        self.directory_name = directory_name
        # The region ID of the directory.
        self.region = region
        # The time when the directory was modified.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name

        if self.region is not None:
            result['Region'] = self.region

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

