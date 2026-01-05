# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeExtensionsResponseBody(DaraModel):
    def __init__(
        self,
        installed_extensions: List[main_models.DescribeExtensionsResponseBodyInstalledExtensions] = None,
        overview: str = None,
        request_id: str = None,
        uninstalled_extensions: List[main_models.DescribeExtensionsResponseBodyUninstalledExtensions] = None,
    ):
        self.installed_extensions = installed_extensions
        self.overview = overview
        # Id of the request
        self.request_id = request_id
        self.uninstalled_extensions = uninstalled_extensions

    def validate(self):
        if self.installed_extensions:
            for v1 in self.installed_extensions:
                 if v1:
                    v1.validate()
        if self.uninstalled_extensions:
            for v1 in self.uninstalled_extensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstalledExtensions'] = []
        if self.installed_extensions is not None:
            for k1 in self.installed_extensions:
                result['InstalledExtensions'].append(k1.to_map() if k1 else None)

        if self.overview is not None:
            result['Overview'] = self.overview

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UninstalledExtensions'] = []
        if self.uninstalled_extensions is not None:
            for k1 in self.uninstalled_extensions:
                result['UninstalledExtensions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.installed_extensions = []
        if m.get('InstalledExtensions') is not None:
            for k1 in m.get('InstalledExtensions'):
                temp_model = main_models.DescribeExtensionsResponseBodyInstalledExtensions()
                self.installed_extensions.append(temp_model.from_map(k1))

        if m.get('Overview') is not None:
            self.overview = m.get('Overview')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.uninstalled_extensions = []
        if m.get('UninstalledExtensions') is not None:
            for k1 in m.get('UninstalledExtensions'):
                temp_model = main_models.DescribeExtensionsResponseBodyUninstalledExtensions()
                self.uninstalled_extensions.append(temp_model.from_map(k1))

        return self

class DescribeExtensionsResponseBodyUninstalledExtensions(DaraModel):
    def __init__(
        self,
        category: str = None,
        comment: str = None,
        default_version: str = None,
        installed_version: str = None,
        name: str = None,
        owner: str = None,
        priority: str = None,
        requires: str = None,
        restart: str = None,
    ):
        self.category = category
        self.comment = comment
        self.default_version = default_version
        self.installed_version = installed_version
        self.name = name
        self.owner = owner
        self.priority = priority
        self.requires = requires
        self.restart = restart

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version

        if self.installed_version is not None:
            result['InstalledVersion'] = self.installed_version

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.requires is not None:
            result['Requires'] = self.requires

        if self.restart is not None:
            result['Restart'] = self.restart

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')

        if m.get('InstalledVersion') is not None:
            self.installed_version = m.get('InstalledVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Requires') is not None:
            self.requires = m.get('Requires')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        return self

class DescribeExtensionsResponseBodyInstalledExtensions(DaraModel):
    def __init__(
        self,
        category: str = None,
        comment: str = None,
        default_version: str = None,
        installed_version: str = None,
        name: str = None,
        owner: str = None,
        priority: str = None,
        requires: str = None,
        restart: str = None,
    ):
        self.category = category
        self.comment = comment
        self.default_version = default_version
        self.installed_version = installed_version
        self.name = name
        self.owner = owner
        self.priority = priority
        self.requires = requires
        self.restart = restart

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version

        if self.installed_version is not None:
            result['InstalledVersion'] = self.installed_version

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.requires is not None:
            result['Requires'] = self.requires

        if self.restart is not None:
            result['Restart'] = self.restart

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')

        if m.get('InstalledVersion') is not None:
            self.installed_version = m.get('InstalledVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Requires') is not None:
            self.requires = m.get('Requires')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        return self

