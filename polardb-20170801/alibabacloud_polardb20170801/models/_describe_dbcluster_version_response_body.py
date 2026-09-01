# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterVersionResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dblatest_stable_version: str = None,
        dblatest_version: str = None,
        dbminor_version: str = None,
        dbrevision_version: str = None,
        dbrevision_version_list: List[main_models.DescribeDBClusterVersionResponseBodyDBRevisionVersionList] = None,
        dbversion: str = None,
        dbversion_status: str = None,
        is_latest_stable_version: str = None,
        is_latest_version: str = None,
        is_proxy_latest_version: str = None,
        proxy_latest_version: str = None,
        proxy_revision_version: str = None,
        proxy_revision_version_list: List[main_models.DescribeDBClusterVersionResponseBodyProxyRevisionVersionList] = None,
        proxy_version_status: str = None,
        request_id: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The latest stable version of PolarDB for PostgreSQL.
        self.dblatest_stable_version = dblatest_stable_version
        # The latest version of the database kernel engine.
        self.dblatest_version = dblatest_version
        # The minor version number of the database engine.
        # * If `DBVersion` is **8.0**, valid values:
        #     * **8.0.2**
        #     * **8.0.1**
        # * If `DBVersion` is **5.7**, the value is **5.7.28**.
        # 
        # * If `DBVersion` is **5.6**, the value is **5.6.16**.
        self.dbminor_version = dbminor_version
        # The Milvus version number of the database engine.
        # > For PolarDB for MySQL 5.6 clusters, only the `Milvus version` information with a release date later than August 31, 2020 is returned. Otherwise, this parameter is empty. For more information about the minor engine versions of PolarDB for MySQL clusters, see [Release notes](https://help.aliyun.com/document_detail/423884.html).
        self.dbrevision_version = dbrevision_version
        # The list of available upgrade version information.
        self.dbrevision_version_list = dbrevision_version_list
        # The major version number of the database engine. Valid values:
        # * **8.0**
        # * **5.7**
        # * **5.6**
        self.dbversion = dbversion
        # The status of the current database minor version. Valid values:
        # * **Stable**: The current version is stable.
        # * **Old**: The current version is outdated. Upgrade to the latest version.
        # * **HighRisk**: The current version has critical bugs. Upgrade to the latest version immediately.
        # * **Beta**: The current version is a beta version.
        # >For more information about how to upgrade the database minor version, see [Version upgrade](https://help.aliyun.com/document_detail/158572.html).
        self.dbversion_status = dbversion_status
        # Indicates whether the current version is the latest stable version of PolarDB for PostgreSQL.
        self.is_latest_stable_version = is_latest_stable_version
        # Indicates whether the current database kernel DPI engine version is the latest database engine version. Valid values:
        # 
        # -  **true**
        # -  **false**
        self.is_latest_version = is_latest_version
        # Indicates whether the current PolarProxy version is the latest version. Valid values:
        # * **true**
        # * **false**
        self.is_proxy_latest_version = is_proxy_latest_version
        # The latest version of PolarProxy.
        self.proxy_latest_version = proxy_latest_version
        # The version of PolarProxy.
        self.proxy_revision_version = proxy_revision_version
        # The release status of the PolarProxy version. Valid values:
        # 
        # - **Stable**: The current version is stable.
        # - **Old**: The current version is outdated. Upgrading to this version is not recommended.
        # - **HighRisk**: The current version has critical bugs. Upgrading to this version is not recommended.
        # - **Beta**: The current version is a beta version.
        self.proxy_revision_version_list = proxy_revision_version_list
        # The version status of PolarProxy. Valid values:
        # * **Stable**: The current version is stable.
        # * **Old**: The current version is outdated. Upgrade to the latest version.
        # * **HighRisk**: The current version has critical bugs. Upgrade to the latest version immediately.
        # * **Beta**: The current version is a beta version.
        # >For more information about how to upgrade the PolarProxy version, see [Version upgrade](https://help.aliyun.com/document_detail/158572.html).
        self.proxy_version_status = proxy_version_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dbrevision_version_list:
            for v1 in self.dbrevision_version_list:
                 if v1:
                    v1.validate()
        if self.proxy_revision_version_list:
            for v1 in self.proxy_revision_version_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dblatest_stable_version is not None:
            result['DBLatestStableVersion'] = self.dblatest_stable_version

        if self.dblatest_version is not None:
            result['DBLatestVersion'] = self.dblatest_version

        if self.dbminor_version is not None:
            result['DBMinorVersion'] = self.dbminor_version

        if self.dbrevision_version is not None:
            result['DBRevisionVersion'] = self.dbrevision_version

        result['DBRevisionVersionList'] = []
        if self.dbrevision_version_list is not None:
            for k1 in self.dbrevision_version_list:
                result['DBRevisionVersionList'].append(k1.to_map() if k1 else None)

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.dbversion_status is not None:
            result['DBVersionStatus'] = self.dbversion_status

        if self.is_latest_stable_version is not None:
            result['IsLatestStableVersion'] = self.is_latest_stable_version

        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version

        if self.is_proxy_latest_version is not None:
            result['IsProxyLatestVersion'] = self.is_proxy_latest_version

        if self.proxy_latest_version is not None:
            result['ProxyLatestVersion'] = self.proxy_latest_version

        if self.proxy_revision_version is not None:
            result['ProxyRevisionVersion'] = self.proxy_revision_version

        result['ProxyRevisionVersionList'] = []
        if self.proxy_revision_version_list is not None:
            for k1 in self.proxy_revision_version_list:
                result['ProxyRevisionVersionList'].append(k1.to_map() if k1 else None)

        if self.proxy_version_status is not None:
            result['ProxyVersionStatus'] = self.proxy_version_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBLatestStableVersion') is not None:
            self.dblatest_stable_version = m.get('DBLatestStableVersion')

        if m.get('DBLatestVersion') is not None:
            self.dblatest_version = m.get('DBLatestVersion')

        if m.get('DBMinorVersion') is not None:
            self.dbminor_version = m.get('DBMinorVersion')

        if m.get('DBRevisionVersion') is not None:
            self.dbrevision_version = m.get('DBRevisionVersion')

        self.dbrevision_version_list = []
        if m.get('DBRevisionVersionList') is not None:
            for k1 in m.get('DBRevisionVersionList'):
                temp_model = main_models.DescribeDBClusterVersionResponseBodyDBRevisionVersionList()
                self.dbrevision_version_list.append(temp_model.from_map(k1))

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('DBVersionStatus') is not None:
            self.dbversion_status = m.get('DBVersionStatus')

        if m.get('IsLatestStableVersion') is not None:
            self.is_latest_stable_version = m.get('IsLatestStableVersion')

        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')

        if m.get('IsProxyLatestVersion') is not None:
            self.is_proxy_latest_version = m.get('IsProxyLatestVersion')

        if m.get('ProxyLatestVersion') is not None:
            self.proxy_latest_version = m.get('ProxyLatestVersion')

        if m.get('ProxyRevisionVersion') is not None:
            self.proxy_revision_version = m.get('ProxyRevisionVersion')

        self.proxy_revision_version_list = []
        if m.get('ProxyRevisionVersionList') is not None:
            for k1 in m.get('ProxyRevisionVersionList'):
                temp_model = main_models.DescribeDBClusterVersionResponseBodyProxyRevisionVersionList()
                self.proxy_revision_version_list.append(temp_model.from_map(k1))

        if m.get('ProxyVersionStatus') is not None:
            self.proxy_version_status = m.get('ProxyVersionStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBClusterVersionResponseBodyProxyRevisionVersionList(DaraModel):
    def __init__(
        self,
        release_note: str = None,
        release_type: str = None,
        revision_version_code: str = None,
        revision_version_name: str = None,
    ):
        # The release notes for the version.
        self.release_note = release_note
        # The release type. Valid values:
        # * **LTS**: Long-term support version.
        # * **BETA**: Preview version.
        self.release_type = release_type
        # The revision version code of the PolarProxy engine, which is used to specify the target version for the upgrade.
        self.revision_version_code = revision_version_code
        # The revision version number of the PolarProxy engine.
        self.revision_version_name = revision_version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note

        if self.release_type is not None:
            result['ReleaseType'] = self.release_type

        if self.revision_version_code is not None:
            result['RevisionVersionCode'] = self.revision_version_code

        if self.revision_version_name is not None:
            result['RevisionVersionName'] = self.revision_version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')

        if m.get('ReleaseType') is not None:
            self.release_type = m.get('ReleaseType')

        if m.get('RevisionVersionCode') is not None:
            self.revision_version_code = m.get('RevisionVersionCode')

        if m.get('RevisionVersionName') is not None:
            self.revision_version_name = m.get('RevisionVersionName')

        return self

class DescribeDBClusterVersionResponseBodyDBRevisionVersionList(DaraModel):
    def __init__(
        self,
        release_note: str = None,
        release_type: str = None,
        revision_version_code: str = None,
        revision_version_name: str = None,
    ):
        # The release notes for the version.
        self.release_note = release_note
        # The release status of the database version. Valid values:
        # * **Stable**: The current version is stable.
        # * **Old**: The current version is outdated. Upgrading to this version is not recommended.
        # * **HighRisk**: The current version has critical bugs. Upgrading to this version is not recommended.
        # * **Beta**: The current version is a beta version.
        self.release_type = release_type
        # The revision version code of the database engine, which is used to specify the target version for the upgrade.
        self.revision_version_code = revision_version_code
        # The revision version number of the database engine.
        self.revision_version_name = revision_version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note

        if self.release_type is not None:
            result['ReleaseType'] = self.release_type

        if self.revision_version_code is not None:
            result['RevisionVersionCode'] = self.revision_version_code

        if self.revision_version_name is not None:
            result['RevisionVersionName'] = self.revision_version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')

        if m.get('ReleaseType') is not None:
            self.release_type = m.get('ReleaseType')

        if m.get('RevisionVersionCode') is not None:
            self.revision_version_code = m.get('RevisionVersionCode')

        if m.get('RevisionVersionName') is not None:
            self.revision_version_name = m.get('RevisionVersionName')

        return self

