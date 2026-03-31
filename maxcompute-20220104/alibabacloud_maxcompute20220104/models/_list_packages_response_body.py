# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListPackagesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListPackagesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListPackagesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListPackagesResponseBodyData(DaraModel):
    def __init__(
        self,
        created_packages: List[main_models.ListPackagesResponseBodyDataCreatedPackages] = None,
        installed_packages: List[main_models.ListPackagesResponseBodyDataInstalledPackages] = None,
    ):
        # The packages that were created.
        self.created_packages = created_packages
        # The packages that were installed.
        self.installed_packages = installed_packages

    def validate(self):
        if self.created_packages:
            for v1 in self.created_packages:
                 if v1:
                    v1.validate()
        if self.installed_packages:
            for v1 in self.installed_packages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['createdPackages'] = []
        if self.created_packages is not None:
            for k1 in self.created_packages:
                result['createdPackages'].append(k1.to_map() if k1 else None)

        result['installedPackages'] = []
        if self.installed_packages is not None:
            for k1 in self.installed_packages:
                result['installedPackages'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.created_packages = []
        if m.get('createdPackages') is not None:
            for k1 in m.get('createdPackages'):
                temp_model = main_models.ListPackagesResponseBodyDataCreatedPackages()
                self.created_packages.append(temp_model.from_map(k1))

        self.installed_packages = []
        if m.get('installedPackages') is not None:
            for k1 in m.get('installedPackages'):
                temp_model = main_models.ListPackagesResponseBodyDataInstalledPackages()
                self.installed_packages.append(temp_model.from_map(k1))

        return self

class ListPackagesResponseBodyDataInstalledPackages(DaraModel):
    def __init__(
        self,
        install_time: int = None,
        name: str = None,
        source_project: str = None,
        status: str = None,
    ):
        # The time when the package was installed.
        self.install_time = install_time
        # The name of the package.
        self.name = name
        # The project to which the package belongs. This parameter is required if the package is installed in the MaxCompute project.
        self.source_project = source_project
        # The status of the package.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.install_time is not None:
            result['installTime'] = self.install_time

        if self.name is not None:
            result['name'] = self.name

        if self.source_project is not None:
            result['sourceProject'] = self.source_project

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('installTime') is not None:
            self.install_time = m.get('installTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceProject') is not None:
            self.source_project = m.get('sourceProject')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class ListPackagesResponseBodyDataCreatedPackages(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        name: str = None,
    ):
        # The time when the package was created.
        self.create_time = create_time
        # The name of the package.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

