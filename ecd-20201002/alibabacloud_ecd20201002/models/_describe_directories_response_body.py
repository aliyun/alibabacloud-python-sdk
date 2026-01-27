# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20201002 import models as main_models
from darabonba.model import DaraModel

class DescribeDirectoriesResponseBody(DaraModel):
    def __init__(
        self,
        directories: List[main_models.DescribeDirectoriesResponseBodyDirectories] = None,
        request_id: str = None,
    ):
        # The directories.
        self.directories = directories
        # The request ID.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.directories = []
        if m.get('Directories') is not None:
            for k1 in m.get('Directories'):
                temp_model = main_models.DescribeDirectoriesResponseBodyDirectories()
                self.directories.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self



class DescribeDirectoriesResponseBodyDirectories(DaraModel):
    def __init__(
        self,
        desktop_access_type: str = None,
        directory_id: str = None,
        directory_type: str = None,
        provider_id: str = None,
        sso_service_url: str = None,
    ):
        # The connection method.
        # 
        # Valid values:
        # 
        # *   VPC: End users connect to cloud computers over an enterprise virtual private cloud (VPC).
        # *   INTERNET: End users connect to cloud computers over the Internet.
        # *   ANY: End users connect to cloud computers over the Internet or an enterprise VPC.
        self.desktop_access_type = desktop_access_type
        # The directory ID.
        self.directory_id = directory_id
        # The directory type.
        self.directory_type = directory_type
        # The provider ID.
        self.provider_id = provider_id
        # The URL of the SSO service.
        self.sso_service_url = sso_service_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type

        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id

        if self.sso_service_url is not None:
            result['SsoServiceUrl'] = self.sso_service_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')

        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')

        if m.get('SsoServiceUrl') is not None:
            self.sso_service_url = m.get('SsoServiceUrl')

        return self

