# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class ListInstalledSoftwaresResponseBody(DaraModel):
    def __init__(
        self,
        additional_packages: main_models.ListInstalledSoftwaresResponseBodyAdditionalPackages = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The list of installed software.
        self.additional_packages = additional_packages
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.additional_packages:
            self.additional_packages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_packages is not None:
            result['AdditionalPackages'] = self.additional_packages.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalPackages') is not None:
            temp_model = main_models.ListInstalledSoftwaresResponseBodyAdditionalPackages()
            self.additional_packages = temp_model.from_map(m.get('AdditionalPackages'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstalledSoftwaresResponseBodyAdditionalPackages(DaraModel):
    def __init__(
        self,
        additional_package_infos: List[main_models.ListInstalledSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfos] = None,
    ):
        self.additional_package_infos = additional_package_infos

    def validate(self):
        if self.additional_package_infos:
            for v1 in self.additional_package_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdditionalPackageInfos'] = []
        if self.additional_package_infos is not None:
            for k1 in self.additional_package_infos:
                result['AdditionalPackageInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_package_infos = []
        if m.get('AdditionalPackageInfos') is not None:
            for k1 in m.get('AdditionalPackageInfos'):
                temp_model = main_models.ListInstalledSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfos()
                self.additional_package_infos.append(temp_model.from_map(k1))

        return self

class ListInstalledSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfos(DaraModel):
    def __init__(
        self,
        category: str = None,
        create_time: str = None,
        description: str = None,
        icon: str = None,
        name: str = None,
        status: str = None,
        version: str = None,
    ):
        # The category into which the software falls.
        self.category = category
        # The time when the software was installed.
        self.create_time = create_time
        # The software description.
        self.description = description
        # The URL of the software icon.
        self.icon = icon
        # The software name.
        self.name = name
        # The installation status of the software.
        # 
        # Valid values:
        # 
        # *   Installed
        # *   Uninstalled
        # *   Installing
        # *   Exception
        self.status = status
        # The software version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

