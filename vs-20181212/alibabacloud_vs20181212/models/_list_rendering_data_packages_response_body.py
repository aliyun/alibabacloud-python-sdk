# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class ListRenderingDataPackagesResponseBody(DaraModel):
    def __init__(
        self,
        data_packages: List[main_models.ListRenderingDataPackagesResponseBodyDataPackages] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data_packages = data_packages
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data_packages:
            for v1 in self.data_packages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataPackages'] = []
        if self.data_packages is not None:
            for k1 in self.data_packages:
                result['DataPackages'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_packages = []
        if m.get('DataPackages') is not None:
            for k1 in m.get('DataPackages'):
                temp_model = main_models.ListRenderingDataPackagesResponseBodyDataPackages()
                self.data_packages.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRenderingDataPackagesResponseBodyDataPackages(DaraModel):
    def __init__(
        self,
        category: str = None,
        creation_time: str = None,
        data_package_id: str = None,
        description: str = None,
        rendering_instance_id: str = None,
        size: int = None,
        status: str = None,
        update_time: str = None,
    ):
        self.category = category
        self.creation_time = creation_time
        self.data_package_id = data_package_id
        self.description = description
        self.rendering_instance_id = rendering_instance_id
        self.size = size
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.data_package_id is not None:
            result['DataPackageId'] = self.data_package_id

        if self.description is not None:
            result['Description'] = self.description

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DataPackageId') is not None:
            self.data_package_id = m.get('DataPackageId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

