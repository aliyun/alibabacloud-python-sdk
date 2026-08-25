# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSoftwarelibVersionRequest(DaraModel):
    def __init__(
        self,
        md_5: str = None,
        os: str = None,
        publisher_type: str = None,
        software_id: str = None,
        software_name: str = None,
        software_pkg_name: str = None,
        software_pkg_size: int = None,
        software_url: str = None,
        software_version: str = None,
    ):
        # The MD5 value of the software package. The value can be up to 64 characters in length.
        self.md_5 = md_5
        # The operating system to which the software package applies. Valid values:
        # - **Windows**: Windows.
        # - **Mac(Apple)**: macOS with Apple silicon.
        # - **Mac(Intel)**: macOS with Intel processors.
        self.os = os
        # The software publisher type. Valid values:
        # - **local**: local upload.
        # - **thirdparty**: third-party link.
        self.publisher_type = publisher_type
        # The software ID in the software library. The value can be up to 64 characters in length. You can call [ListSoftwarelibSoftware](~~ListSoftwarelibSoftware~~) to obtain the value.
        # 
        # This parameter is required.
        self.software_id = software_id
        # The software name. The value can be up to 128 characters in length.
        self.software_name = software_name
        # The file name of the software package. The value can be up to 128 characters in length.
        self.software_pkg_name = software_pkg_name
        # The size of the software package.
        self.software_pkg_size = software_pkg_size
        # The download URL of the software package. If the publisher type is local, the value is the relative path of the software package in the OSS bucket. If the publisher type is thirdparty, the value is a third-party download URL.
        self.software_url = software_url
        # The software version number. The value can be up to 64 characters in length. The combination of operating system and version number must be unique within the same software. If a duplicate exists, a ResourceDuplicated error is returned.
        self.software_version = software_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.os is not None:
            result['Os'] = self.os

        if self.publisher_type is not None:
            result['PublisherType'] = self.publisher_type

        if self.software_id is not None:
            result['SoftwareId'] = self.software_id

        if self.software_name is not None:
            result['SoftwareName'] = self.software_name

        if self.software_pkg_name is not None:
            result['SoftwarePkgName'] = self.software_pkg_name

        if self.software_pkg_size is not None:
            result['SoftwarePkgSize'] = self.software_pkg_size

        if self.software_url is not None:
            result['SoftwareUrl'] = self.software_url

        if self.software_version is not None:
            result['SoftwareVersion'] = self.software_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('PublisherType') is not None:
            self.publisher_type = m.get('PublisherType')

        if m.get('SoftwareId') is not None:
            self.software_id = m.get('SoftwareId')

        if m.get('SoftwareName') is not None:
            self.software_name = m.get('SoftwareName')

        if m.get('SoftwarePkgName') is not None:
            self.software_pkg_name = m.get('SoftwarePkgName')

        if m.get('SoftwarePkgSize') is not None:
            self.software_pkg_size = m.get('SoftwarePkgSize')

        if m.get('SoftwareUrl') is not None:
            self.software_url = m.get('SoftwareUrl')

        if m.get('SoftwareVersion') is not None:
            self.software_version = m.get('SoftwareVersion')

        return self

