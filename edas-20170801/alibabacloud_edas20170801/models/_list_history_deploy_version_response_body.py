# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListHistoryDeployVersionResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        package_version_list: main_models.ListHistoryDeployVersionResponseBodyPackageVersionList = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The additional information that is returned.
        self.message = message
        self.package_version_list = package_version_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.package_version_list:
            self.package_version_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.package_version_list is not None:
            result['PackageVersionList'] = self.package_version_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PackageVersionList') is not None:
            temp_model = main_models.ListHistoryDeployVersionResponseBodyPackageVersionList()
            self.package_version_list = temp_model.from_map(m.get('PackageVersionList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListHistoryDeployVersionResponseBodyPackageVersionList(DaraModel):
    def __init__(
        self,
        package_version: List[main_models.ListHistoryDeployVersionResponseBodyPackageVersionListPackageVersion] = None,
    ):
        self.package_version = package_version

    def validate(self):
        if self.package_version:
            for v1 in self.package_version:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PackageVersion'] = []
        if self.package_version is not None:
            for k1 in self.package_version:
                result['PackageVersion'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.package_version = []
        if m.get('PackageVersion') is not None:
            for k1 in m.get('PackageVersion'):
                temp_model = main_models.ListHistoryDeployVersionResponseBodyPackageVersionListPackageVersion()
                self.package_version.append(temp_model.from_map(k1))

        return self

class ListHistoryDeployVersionResponseBodyPackageVersionListPackageVersion(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: int = None,
        description: str = None,
        id: str = None,
        package_version: str = None,
        public_url: str = None,
        type: str = None,
        update_time: int = None,
        war_url: str = None,
    ):
        self.app_id = app_id
        self.create_time = create_time
        self.description = description
        self.id = id
        self.package_version = package_version
        self.public_url = public_url
        self.type = type
        self.update_time = update_time
        self.war_url = war_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.package_version is not None:
            result['PackageVersion'] = self.package_version

        if self.public_url is not None:
            result['PublicUrl'] = self.public_url

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.war_url is not None:
            result['WarUrl'] = self.war_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')

        if m.get('PublicUrl') is not None:
            self.public_url = m.get('PublicUrl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('WarUrl') is not None:
            self.war_url = m.get('WarUrl')

        return self

