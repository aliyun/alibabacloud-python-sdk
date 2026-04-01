# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribePostgresExtensionsResponseBody(DaraModel):
    def __init__(
        self,
        installed_extensions: List[main_models.DescribePostgresExtensionsResponseBodyInstalledExtensions] = None,
        overview: Dict[str, Any] = None,
        request_id: str = None,
        uninstalled_extensions: List[main_models.DescribePostgresExtensionsResponseBodyUninstalledExtensions] = None,
    ):
        # The list of extensions that are installed on the specified database.
        self.installed_extensions = installed_extensions
        # The overview of the extension.
        self.overview = overview
        # The request ID.
        self.request_id = request_id
        # The list of extensions that are not installed on the specified database.
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
                temp_model = main_models.DescribePostgresExtensionsResponseBodyInstalledExtensions()
                self.installed_extensions.append(temp_model.from_map(k1))

        if m.get('Overview') is not None:
            self.overview = m.get('Overview')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.uninstalled_extensions = []
        if m.get('UninstalledExtensions') is not None:
            for k1 in m.get('UninstalledExtensions'):
                temp_model = main_models.DescribePostgresExtensionsResponseBodyUninstalledExtensions()
                self.uninstalled_extensions.append(temp_model.from_map(k1))

        return self

class DescribePostgresExtensionsResponseBodyUninstalledExtensions(DaraModel):
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
        uid: str = None,
    ):
        # The category of the extension.
        self.category = category
        # The purpose of the extension.
        self.comment = comment
        # The default version of the extension.
        self.default_version = default_version
        # The current version of the extension.
        self.installed_version = installed_version
        # The name of the extension.
        self.name = name
        # The user of the extension.
        self.owner = owner
        # The priority of the extension.
        self.priority = priority
        # The extensions on which the current extension depends when it is installed.
        self.requires = requires
        # The ID of the Alibaba Cloud account.
        # 
        # >  This parameter is returned only for self-developed exclusive extensions. You can view exclusive extensions only within your Alibaba Cloud account.
        self.uid = uid

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

        if self.uid is not None:
            result['Uid'] = self.uid

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

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

class DescribePostgresExtensionsResponseBodyInstalledExtensions(DaraModel):
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
        uid: str = None,
    ):
        # The category of the extension.
        # 
        # *   **external_access**
        # *   **index_support**
        # *   **information_stat**
        # *   **geography_space**
        # *   **vector_engine**
        # *   **timing_engine**
        # *   **data_type**
        # *   **encrypt_secure**
        # *   **text_process**
        # *   **operation_maintenance**
        # *   **self_develop**
        self.category = category
        # The purpose of the extension.
        self.comment = comment
        # The default version of the extension.
        self.default_version = default_version
        # The current version of the extension.
        self.installed_version = installed_version
        # The name of the extension.
        self.name = name
        # The user of the extension.
        self.owner = owner
        # The priority of the extension.
        # 
        # *   **0**: The extension is displayed by default.
        # *   **1**: The extension is preferentially displayed.
        self.priority = priority
        # The extensions on which the current extension depends when it is installed.
        self.requires = requires
        # The ID of the Alibaba Cloud account.
        # 
        # >  This parameter is returned only for self-developed exclusive extensions. You can view exclusive extensions only within your Alibaba Cloud account.
        self.uid = uid

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

        if self.uid is not None:
            result['Uid'] = self.uid

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

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

