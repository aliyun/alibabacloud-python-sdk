# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListSoftwarelibSoftwareResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.ListSoftwarelibSoftwareResponseBodyDataList] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The software list.
        self.data_list = data_list
        # The maximum number of entries per page. This parameter is not returned by this operation.
        self.max_results = max_results
        # The pagination token. This parameter is not returned by this operation.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # The total number of software entries that match the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.ListSoftwarelibSoftwareResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSoftwarelibSoftwareResponseBodyDataList(DaraModel):
    def __init__(
        self,
        builtin_software_id: str = None,
        check_bundle_id: str = None,
        check_software_name: str = None,
        classify_id: str = None,
        create_time: str = None,
        description: str = None,
        dev_tags: List[str] = None,
        device_group_ids: List[str] = None,
        download_times: int = None,
        has_new_version: bool = None,
        logo_url: str = None,
        mac_apple_version: str = None,
        mac_intel_version: str = None,
        match_mode: str = None,
        official_download_url: str = None,
        software_id: str = None,
        software_name: str = None,
        source_removed: bool = None,
        source_type: str = None,
        user_group_ids: List[str] = None,
        versions: List[main_models.ListSoftwarelibSoftwareResponseBodyDataListVersions] = None,
        windows_version: str = None,
    ):
        # The associated built-in software ID.
        self.builtin_software_id = builtin_software_id
        # The software BundleId used for verification.
        self.check_bundle_id = check_bundle_id
        # The software name used for verification.
        self.check_software_name = check_software_name
        # The software classification ID.
        self.classify_id = classify_id
        # The time when the software was created, in seconds-level UNIX timestamp.
        self.create_time = create_time
        # The software description.
        self.description = description
        # The list of associated terminal device IDs.
        self.dev_tags = dev_tags
        # The list of associated device group IDs.
        self.device_group_ids = device_group_ids
        # The number of times the software has been manually downloaded from the client.
        self.download_times = download_times
        # Indicates whether a new version is available for the software.
        self.has_new_version = has_new_version
        # The URL of the software logo.
        self.logo_url = logo_url
        # The latest software version number for Mac (Apple).
        self.mac_apple_version = mac_apple_version
        # The latest software version number for Mac (Intel).
        self.mac_intel_version = mac_intel_version
        # The policy matching target type. Valid values:
        # - **UserGroupAll**: all users.
        # - **UserGroupNormal**: specified user groups.
        # - **DevTagNormal**: specified devices.
        # - **DeviceGroupNormal**: specified device groups.
        # - **DevTagAll**: all devices.
        # - **None**: not configured.
        self.match_mode = match_mode
        # The official download URL of the software.
        self.official_download_url = official_download_url
        # The software ID.
        self.software_id = software_id
        # The software name.
        self.software_name = software_name
        # Indicates whether the built-in library source has been removed.
        self.source_removed = source_removed
        # The software source. Valid values:
        # - **custom**: custom software.
        # - **builtin**: built-in software library.
        self.source_type = source_type
        # The list of associated user group IDs.
        self.user_group_ids = user_group_ids
        # The software version list. This field is not returned by this operation. Call [ListSoftwarelibVersion](~~ListSoftwarelibVersion~~) to query software versions.
        self.versions = versions
        # The latest software version number for Windows.
        self.windows_version = windows_version

    def validate(self):
        if self.versions:
            for v1 in self.versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.builtin_software_id is not None:
            result['BuiltinSoftwareId'] = self.builtin_software_id

        if self.check_bundle_id is not None:
            result['CheckBundleId'] = self.check_bundle_id

        if self.check_software_name is not None:
            result['CheckSoftwareName'] = self.check_software_name

        if self.classify_id is not None:
            result['ClassifyId'] = self.classify_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.dev_tags is not None:
            result['DevTags'] = self.dev_tags

        if self.device_group_ids is not None:
            result['DeviceGroupIds'] = self.device_group_ids

        if self.download_times is not None:
            result['DownloadTimes'] = self.download_times

        if self.has_new_version is not None:
            result['HasNewVersion'] = self.has_new_version

        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url

        if self.mac_apple_version is not None:
            result['MacAppleVersion'] = self.mac_apple_version

        if self.mac_intel_version is not None:
            result['MacIntelVersion'] = self.mac_intel_version

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.official_download_url is not None:
            result['OfficialDownloadUrl'] = self.official_download_url

        if self.software_id is not None:
            result['SoftwareId'] = self.software_id

        if self.software_name is not None:
            result['SoftwareName'] = self.software_name

        if self.source_removed is not None:
            result['SourceRemoved'] = self.source_removed

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        result['Versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['Versions'].append(k1.to_map() if k1 else None)

        if self.windows_version is not None:
            result['WindowsVersion'] = self.windows_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuiltinSoftwareId') is not None:
            self.builtin_software_id = m.get('BuiltinSoftwareId')

        if m.get('CheckBundleId') is not None:
            self.check_bundle_id = m.get('CheckBundleId')

        if m.get('CheckSoftwareName') is not None:
            self.check_software_name = m.get('CheckSoftwareName')

        if m.get('ClassifyId') is not None:
            self.classify_id = m.get('ClassifyId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DevTags') is not None:
            self.dev_tags = m.get('DevTags')

        if m.get('DeviceGroupIds') is not None:
            self.device_group_ids = m.get('DeviceGroupIds')

        if m.get('DownloadTimes') is not None:
            self.download_times = m.get('DownloadTimes')

        if m.get('HasNewVersion') is not None:
            self.has_new_version = m.get('HasNewVersion')

        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')

        if m.get('MacAppleVersion') is not None:
            self.mac_apple_version = m.get('MacAppleVersion')

        if m.get('MacIntelVersion') is not None:
            self.mac_intel_version = m.get('MacIntelVersion')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('OfficialDownloadUrl') is not None:
            self.official_download_url = m.get('OfficialDownloadUrl')

        if m.get('SoftwareId') is not None:
            self.software_id = m.get('SoftwareId')

        if m.get('SoftwareName') is not None:
            self.software_name = m.get('SoftwareName')

        if m.get('SourceRemoved') is not None:
            self.source_removed = m.get('SourceRemoved')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        self.versions = []
        if m.get('Versions') is not None:
            for k1 in m.get('Versions'):
                temp_model = main_models.ListSoftwarelibSoftwareResponseBodyDataListVersions()
                self.versions.append(temp_model.from_map(k1))

        if m.get('WindowsVersion') is not None:
            self.windows_version = m.get('WindowsVersion')

        return self

class ListSoftwarelibSoftwareResponseBodyDataListVersions(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        download_times: int = None,
        md_5: str = None,
        modify_time: str = None,
        os: str = None,
        publisher_type: str = None,
        software_id: str = None,
        software_pkg_name: str = None,
        software_pkg_size: int = None,
        software_url: str = None,
        status: str = None,
        version: str = None,
        version_id: str = None,
    ):
        # The time when the software version was created.
        self.create_time = create_time
        # The number of times the software has been downloaded from the client.
        self.download_times = download_times
        # The MD5 value of the software package.
        self.md_5 = md_5
        # The time when the software version was last modified.
        self.modify_time = modify_time
        # The operating system to which the software package applies. Valid values:
        # - **Windows**: Windows.
        # - **Mac(Apple)**: macOS with Apple silicon.
        # - **Mac(Intel)**: macOS with Intel processors.
        self.os = os
        # The software publisher type. Valid values:
        # - **local**: locally uploaded.
        # - **thirdparty**: third-party link.
        self.publisher_type = publisher_type
        # The ID of the software to which the version belongs.
        self.software_id = software_id
        # The name of the software package.
        self.software_pkg_name = software_pkg_name
        # The size of the software package.
        self.software_pkg_size = software_pkg_size
        # The download URL of the software package.
        self.software_url = software_url
        # The version publish status. Valid values:
        # - **published**: Published.
        # - **unpublished**: Not published.
        self.status = status
        # The software version number.
        self.version = version
        # The software version ID.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.download_times is not None:
            result['DownloadTimes'] = self.download_times

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.os is not None:
            result['Os'] = self.os

        if self.publisher_type is not None:
            result['PublisherType'] = self.publisher_type

        if self.software_id is not None:
            result['SoftwareId'] = self.software_id

        if self.software_pkg_name is not None:
            result['SoftwarePkgName'] = self.software_pkg_name

        if self.software_pkg_size is not None:
            result['SoftwarePkgSize'] = self.software_pkg_size

        if self.software_url is not None:
            result['SoftwareUrl'] = self.software_url

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DownloadTimes') is not None:
            self.download_times = m.get('DownloadTimes')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('PublisherType') is not None:
            self.publisher_type = m.get('PublisherType')

        if m.get('SoftwareId') is not None:
            self.software_id = m.get('SoftwareId')

        if m.get('SoftwarePkgName') is not None:
            self.software_pkg_name = m.get('SoftwarePkgName')

        if m.get('SoftwarePkgSize') is not None:
            self.software_pkg_size = m.get('SoftwarePkgSize')

        if m.get('SoftwareUrl') is not None:
            self.software_url = m.get('SoftwareUrl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

