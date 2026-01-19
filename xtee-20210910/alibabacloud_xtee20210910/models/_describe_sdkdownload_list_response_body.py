# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeSDKDownloadListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: List[main_models.DescribeSDKDownloadListResponseBodyResultObject] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeSDKDownloadListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        return self

class DescribeSDKDownloadListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        description: str = None,
        developer: str = None,
        device_type: str = None,
        download_url: str = None,
        md_5: str = None,
        package_name: str = None,
        privacy_link: str = None,
        push_time: str = None,
        sdk_version: str = None,
        size: str = None,
    ):
        # Description information.
        self.description = description
        # Developer
        self.developer = developer
        # Device type.
        self.device_type = device_type
        # Download URL.
        self.download_url = download_url
        # File MD5.
        self.md_5 = md_5
        # Package name
        self.package_name = package_name
        # Risk recognition SDK privacy policy link
        self.privacy_link = privacy_link
        # Release time
        self.push_time = push_time
        # SDK version.
        self.sdk_version = sdk_version
        # Size
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.developer is not None:
            result['developer'] = self.developer

        if self.device_type is not None:
            result['deviceType'] = self.device_type

        if self.download_url is not None:
            result['downloadUrl'] = self.download_url

        if self.md_5 is not None:
            result['md5'] = self.md_5

        if self.package_name is not None:
            result['packageName'] = self.package_name

        if self.privacy_link is not None:
            result['privacyLink'] = self.privacy_link

        if self.push_time is not None:
            result['pushTime'] = self.push_time

        if self.sdk_version is not None:
            result['sdkVersion'] = self.sdk_version

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('developer') is not None:
            self.developer = m.get('developer')

        if m.get('deviceType') is not None:
            self.device_type = m.get('deviceType')

        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')

        if m.get('md5') is not None:
            self.md_5 = m.get('md5')

        if m.get('packageName') is not None:
            self.package_name = m.get('packageName')

        if m.get('privacyLink') is not None:
            self.privacy_link = m.get('privacyLink')

        if m.get('pushTime') is not None:
            self.push_time = m.get('pushTime')

        if m.get('sdkVersion') is not None:
            self.sdk_version = m.get('sdkVersion')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

