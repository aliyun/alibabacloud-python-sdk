# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeEngineVersionResponseBody(DaraModel):
    def __init__(
        self,
        dblatest_minor_version: main_models.DescribeEngineVersionResponseBodyDBLatestMinorVersion = None,
        dbversion_release: str = None,
        enable_upgrade_major_version: bool = None,
        enable_upgrade_minor_version: bool = None,
        engine: str = None,
        is_auto_upgrade_open: str = None,
        is_latest_version: bool = None,
        is_new_sslmode: str = None,
        is_open_nglb: str = None,
        is_redis_compatible_version: str = None,
        is_sslenable: str = None,
        major_version: str = None,
        minor_version: str = None,
        proxy_latest_minor_version: main_models.DescribeEngineVersionResponseBodyProxyLatestMinorVersion = None,
        proxy_minor_version: str = None,
        proxy_version_release: str = None,
        request_id: str = None,
    ):
        # The information about the latest minor version to which the instance can be upgraded.
        self.dblatest_minor_version = dblatest_minor_version
        # The update notes for the minor version of the instance, including the release time, minor version number, type (such as new feature), and detailed description.
        self.dbversion_release = dbversion_release
        # Indicates whether the major version of the instance can be upgraded. Valid values:
        # * **true**: The major version can be upgraded.
        # * **false**: The major version cannot be upgraded, usually because it is already the latest version.
        # 
        # > To upgrade the major version, call the [ModifyInstanceMajorVersion](https://help.aliyun.com/document_detail/473776.html) operation.
        self.enable_upgrade_major_version = enable_upgrade_major_version
        # Indicates whether the minor version of the instance can be upgraded. Valid values:
        # 
        # * **true**: The minor version can be upgraded.
        # * **false**: The minor version is already the latest and cannot be upgraded. 
        # 
        # > To upgrade the minor version, call the [ModifyInstanceMinorVersion](https://help.aliyun.com/document_detail/473777.html) operation.
        self.enable_upgrade_minor_version = enable_upgrade_minor_version
        # The database engine type. Valid values: **redis** and **memcache**.
        self.engine = engine
        # Indicates whether automatic minor version upgrade is enabled. Valid values:
        # 
        # - **0**: Disabled.
        # - **1**: Enabled.
        self.is_auto_upgrade_open = is_auto_upgrade_open
        # Indicates whether the minor version of the instance is the latest. Valid values:
        # * **true**: Yes.
        # * **false**: No.
        self.is_latest_version = is_latest_version
        # Indicates whether the new TLS version is supported. Valid values:
        # * **1**: Enabled.
        # * **0**: Disabled.
        self.is_new_sslmode = is_new_sslmode
        # Indicates whether NGLB mode is enabled. Valid values:
        # * **0**: Disabled.
        # * **1**: Enabled.
        self.is_open_nglb = is_open_nglb
        # Indicates whether the instance is a Redis-compatible version.
        self.is_redis_compatible_version = is_redis_compatible_version
        # Indicates whether SSL is enabled. Valid values:
        # * **1**: Enabled.
        # * **0**: Disabled.
        self.is_sslenable = is_sslenable
        # The major version of the instance.
        self.major_version = major_version
        # The current minor version of the instance.
        self.minor_version = minor_version
        # The information about the latest minor version to which the proxy node can be upgraded.
        self.proxy_latest_minor_version = proxy_latest_minor_version
        # The current minor version of the proxy node.
        # > This parameter is returned only for instances of the cluster or read/write splitting architecture.
        self.proxy_minor_version = proxy_minor_version
        # The update notes for the minor version of the proxy node, including the release time, minor version number, type (such as new feature), and detailed description.
        # > This parameter is returned only for instances of the cluster or read/write splitting architecture.
        self.proxy_version_release = proxy_version_release
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.dblatest_minor_version:
            self.dblatest_minor_version.validate()
        if self.proxy_latest_minor_version:
            self.proxy_latest_minor_version.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dblatest_minor_version is not None:
            result['DBLatestMinorVersion'] = self.dblatest_minor_version.to_map()

        if self.dbversion_release is not None:
            result['DBVersionRelease'] = self.dbversion_release

        if self.enable_upgrade_major_version is not None:
            result['EnableUpgradeMajorVersion'] = self.enable_upgrade_major_version

        if self.enable_upgrade_minor_version is not None:
            result['EnableUpgradeMinorVersion'] = self.enable_upgrade_minor_version

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.is_auto_upgrade_open is not None:
            result['IsAutoUpgradeOpen'] = self.is_auto_upgrade_open

        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version

        if self.is_new_sslmode is not None:
            result['IsNewSSLMode'] = self.is_new_sslmode

        if self.is_open_nglb is not None:
            result['IsOpenNGLB'] = self.is_open_nglb

        if self.is_redis_compatible_version is not None:
            result['IsRedisCompatibleVersion'] = self.is_redis_compatible_version

        if self.is_sslenable is not None:
            result['IsSSLEnable'] = self.is_sslenable

        if self.major_version is not None:
            result['MajorVersion'] = self.major_version

        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version

        if self.proxy_latest_minor_version is not None:
            result['ProxyLatestMinorVersion'] = self.proxy_latest_minor_version.to_map()

        if self.proxy_minor_version is not None:
            result['ProxyMinorVersion'] = self.proxy_minor_version

        if self.proxy_version_release is not None:
            result['ProxyVersionRelease'] = self.proxy_version_release

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBLatestMinorVersion') is not None:
            temp_model = main_models.DescribeEngineVersionResponseBodyDBLatestMinorVersion()
            self.dblatest_minor_version = temp_model.from_map(m.get('DBLatestMinorVersion'))

        if m.get('DBVersionRelease') is not None:
            self.dbversion_release = m.get('DBVersionRelease')

        if m.get('EnableUpgradeMajorVersion') is not None:
            self.enable_upgrade_major_version = m.get('EnableUpgradeMajorVersion')

        if m.get('EnableUpgradeMinorVersion') is not None:
            self.enable_upgrade_minor_version = m.get('EnableUpgradeMinorVersion')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('IsAutoUpgradeOpen') is not None:
            self.is_auto_upgrade_open = m.get('IsAutoUpgradeOpen')

        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')

        if m.get('IsNewSSLMode') is not None:
            self.is_new_sslmode = m.get('IsNewSSLMode')

        if m.get('IsOpenNGLB') is not None:
            self.is_open_nglb = m.get('IsOpenNGLB')

        if m.get('IsRedisCompatibleVersion') is not None:
            self.is_redis_compatible_version = m.get('IsRedisCompatibleVersion')

        if m.get('IsSSLEnable') is not None:
            self.is_sslenable = m.get('IsSSLEnable')

        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')

        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')

        if m.get('ProxyLatestMinorVersion') is not None:
            temp_model = main_models.DescribeEngineVersionResponseBodyProxyLatestMinorVersion()
            self.proxy_latest_minor_version = temp_model.from_map(m.get('ProxyLatestMinorVersion'))

        if m.get('ProxyMinorVersion') is not None:
            self.proxy_minor_version = m.get('ProxyMinorVersion')

        if m.get('ProxyVersionRelease') is not None:
            self.proxy_version_release = m.get('ProxyVersionRelease')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEngineVersionResponseBodyProxyLatestMinorVersion(DaraModel):
    def __init__(
        self,
        level: str = None,
        minor_version: str = None,
        version_release: main_models.DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionRelease = None,
    ):
        # The importance level of the version change. Valid values:
        # * **0**: Normal.
        # * **1**: Important.
        # * **2**: Critical.
        self.level = level
        # The version number.
        self.minor_version = minor_version
        # The version evolution path from the current minor version of the instance to the latest minor version. This is consistent with the version documentation. You can refer to the version release notes for more detailed information.
        self.version_release = version_release

    def validate(self):
        if self.version_release:
            self.version_release.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level is not None:
            result['Level'] = self.level

        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version

        if self.version_release is not None:
            result['VersionRelease'] = self.version_release.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')

        if m.get('VersionRelease') is not None:
            temp_model = main_models.DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionRelease()
            self.version_release = temp_model.from_map(m.get('VersionRelease'))

        return self

class DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionRelease(DaraModel):
    def __init__(
        self,
        release_info: main_models.DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionReleaseReleaseInfo = None,
        version_changes_level: str = None,
    ):
        self.release_info = release_info
        # The importance level of the version upgrade (recommended upgrade level). Valid values:
        # * 0: Normal.
        # * 1: Important.
        # * 2: Critical.
        self.version_changes_level = version_changes_level

    def validate(self):
        if self.release_info:
            self.release_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.release_info is not None:
            result['ReleaseInfo'] = self.release_info.to_map()

        if self.version_changes_level is not None:
            result['VersionChangesLevel'] = self.version_changes_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReleaseInfo') is not None:
            temp_model = main_models.DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionReleaseReleaseInfo()
            self.release_info = temp_model.from_map(m.get('ReleaseInfo'))

        if m.get('VersionChangesLevel') is not None:
            self.version_changes_level = m.get('VersionChangesLevel')

        return self

class DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionReleaseReleaseInfo(DaraModel):
    def __init__(
        self,
        release_info_list: List[main_models.DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionReleaseReleaseInfoReleaseInfoList] = None,
    ):
        self.release_info_list = release_info_list

    def validate(self):
        if self.release_info_list:
            for v1 in self.release_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ReleaseInfoList'] = []
        if self.release_info_list is not None:
            for k1 in self.release_info_list:
                result['ReleaseInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.release_info_list = []
        if m.get('ReleaseInfoList') is not None:
            for k1 in m.get('ReleaseInfoList'):
                temp_model = main_models.DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionReleaseReleaseInfoReleaseInfoList()
                self.release_info_list.append(temp_model.from_map(k1))

        return self

class DescribeEngineVersionResponseBodyProxyLatestMinorVersionVersionReleaseReleaseInfoReleaseInfoList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        level: str = None,
        release_note: str = None,
        release_note_en: str = None,
        release_version: str = None,
    ):
        self.create_time = create_time
        self.level = level
        self.release_note = release_note
        self.release_note_en = release_note_en
        self.release_version = release_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.level is not None:
            result['Level'] = self.level

        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note

        if self.release_note_en is not None:
            result['ReleaseNoteEn'] = self.release_note_en

        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')

        if m.get('ReleaseNoteEn') is not None:
            self.release_note_en = m.get('ReleaseNoteEn')

        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')

        return self

class DescribeEngineVersionResponseBodyDBLatestMinorVersion(DaraModel):
    def __init__(
        self,
        level: str = None,
        minor_version: str = None,
        version_release: main_models.DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionRelease = None,
    ):
        # The importance level of the version change. Valid values:
        # * **0**: Normal.
        # * **1**: Important.
        # * **2**: Critical.
        self.level = level
        # The version number.
        self.minor_version = minor_version
        # The version evolution path from the current minor version of the instance to the latest minor version. This is consistent with the version documentation. You can refer to the version release notes for more detailed information.
        self.version_release = version_release

    def validate(self):
        if self.version_release:
            self.version_release.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level is not None:
            result['Level'] = self.level

        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version

        if self.version_release is not None:
            result['VersionRelease'] = self.version_release.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')

        if m.get('VersionRelease') is not None:
            temp_model = main_models.DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionRelease()
            self.version_release = temp_model.from_map(m.get('VersionRelease'))

        return self

class DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionRelease(DaraModel):
    def __init__(
        self,
        release_info: main_models.DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionReleaseReleaseInfo = None,
        version_changes_level: str = None,
    ):
        self.release_info = release_info
        # The importance level of the version upgrade (recommended upgrade level). Valid values:
        # * 0: Normal.
        # * 1: Important.
        # * 2: Critical.
        self.version_changes_level = version_changes_level

    def validate(self):
        if self.release_info:
            self.release_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.release_info is not None:
            result['ReleaseInfo'] = self.release_info.to_map()

        if self.version_changes_level is not None:
            result['VersionChangesLevel'] = self.version_changes_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReleaseInfo') is not None:
            temp_model = main_models.DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionReleaseReleaseInfo()
            self.release_info = temp_model.from_map(m.get('ReleaseInfo'))

        if m.get('VersionChangesLevel') is not None:
            self.version_changes_level = m.get('VersionChangesLevel')

        return self

class DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionReleaseReleaseInfo(DaraModel):
    def __init__(
        self,
        release_info_list: List[main_models.DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionReleaseReleaseInfoReleaseInfoList] = None,
    ):
        self.release_info_list = release_info_list

    def validate(self):
        if self.release_info_list:
            for v1 in self.release_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ReleaseInfoList'] = []
        if self.release_info_list is not None:
            for k1 in self.release_info_list:
                result['ReleaseInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.release_info_list = []
        if m.get('ReleaseInfoList') is not None:
            for k1 in m.get('ReleaseInfoList'):
                temp_model = main_models.DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionReleaseReleaseInfoReleaseInfoList()
                self.release_info_list.append(temp_model.from_map(k1))

        return self

class DescribeEngineVersionResponseBodyDBLatestMinorVersionVersionReleaseReleaseInfoReleaseInfoList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        level: str = None,
        release_note: str = None,
        release_note_en: str = None,
        release_version: str = None,
    ):
        self.create_time = create_time
        self.level = level
        self.release_note = release_note
        self.release_note_en = release_note_en
        self.release_version = release_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.level is not None:
            result['Level'] = self.level

        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note

        if self.release_note_en is not None:
            result['ReleaseNoteEn'] = self.release_note_en

        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')

        if m.get('ReleaseNoteEn') is not None:
            self.release_note_en = m.get('ReleaseNoteEn')

        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')

        return self

