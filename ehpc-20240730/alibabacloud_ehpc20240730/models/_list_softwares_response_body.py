# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class ListSoftwaresResponseBody(DaraModel):
    def __init__(
        self,
        additional_packages: main_models.ListSoftwaresResponseBodyAdditionalPackages = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The information about the software that can be installed in the cluster.
        self.additional_packages = additional_packages
        # The page number. Pages start from page 1. Default value: 1.
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
            temp_model = main_models.ListSoftwaresResponseBodyAdditionalPackages()
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

class ListSoftwaresResponseBodyAdditionalPackages(DaraModel):
    def __init__(
        self,
        additional_package_infos: List[main_models.ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfos] = None,
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
                temp_model = main_models.ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfos()
                self.additional_package_infos.append(temp_model.from_map(k1))

        return self

class ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfos(DaraModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        icon: str = None,
        name: str = None,
        versions: main_models.ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersions = None,
    ):
        # The application category.
        self.category = category
        # The software description.
        self.description = description
        # The URL of the software icon.
        self.icon = icon
        # The software name.
        self.name = name
        # The information about the software versions that can be installed in the cluster.
        self.versions = versions

    def validate(self):
        if self.versions:
            self.versions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.description is not None:
            result['Description'] = self.description

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.name is not None:
            result['Name'] = self.name

        if self.versions is not None:
            result['Versions'] = self.versions.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Versions') is not None:
            temp_model = main_models.ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersions()
            self.versions = temp_model.from_map(m.get('Versions'))

        return self

class ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersions(DaraModel):
    def __init__(
        self,
        version_infos: List[main_models.ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfos] = None,
    ):
        self.version_infos = version_infos

    def validate(self):
        if self.version_infos:
            for v1 in self.version_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VersionInfos'] = []
        if self.version_infos is not None:
            for k1 in self.version_infos:
                result['VersionInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.version_infos = []
        if m.get('VersionInfos') is not None:
            for k1 in m.get('VersionInfos'):
                temp_model = main_models.ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfos()
                self.version_infos.append(temp_model.from_map(k1))

        return self

class ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfos(DaraModel):
    def __init__(
        self,
        latest: str = None,
        support_os: main_models.ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfosSupportOs = None,
        version: str = None,
    ):
        # Indicates whether the version is the latest.
        self.latest = latest
        # The information about the supported OSs.
        self.support_os = support_os
        # The software version.
        self.version = version

    def validate(self):
        if self.support_os:
            self.support_os.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.latest is not None:
            result['Latest'] = self.latest

        if self.support_os is not None:
            result['SupportOs'] = self.support_os.to_map()

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Latest') is not None:
            self.latest = m.get('Latest')

        if m.get('SupportOs') is not None:
            temp_model = main_models.ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfosSupportOs()
            self.support_os = temp_model.from_map(m.get('SupportOs'))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfosSupportOs(DaraModel):
    def __init__(
        self,
        support_os_infos: List[main_models.ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfosSupportOsSupportOsInfos] = None,
    ):
        self.support_os_infos = support_os_infos

    def validate(self):
        if self.support_os_infos:
            for v1 in self.support_os_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportOsInfos'] = []
        if self.support_os_infos is not None:
            for k1 in self.support_os_infos:
                result['SupportOsInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.support_os_infos = []
        if m.get('SupportOsInfos') is not None:
            for k1 in m.get('SupportOsInfos'):
                temp_model = main_models.ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfosSupportOsSupportOsInfos()
                self.support_os_infos.append(temp_model.from_map(k1))

        return self

class ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfosSupportOsSupportOsInfos(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        os_tag: str = None,
    ):
        # The OS architecture. Valid values:
        # 
        # *   x86_64
        # *   arm64
        self.architecture = architecture
        # The image tag.
        self.os_tag = os_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.os_tag is not None:
            result['OsTag'] = self.os_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')

        return self

