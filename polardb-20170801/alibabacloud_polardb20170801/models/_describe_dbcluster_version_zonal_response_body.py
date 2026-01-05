# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterVersionZonalResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dblatest_version: str = None,
        dbminor_version: str = None,
        dbrevision_version: str = None,
        dbrevision_version_list: List[main_models.DescribeDBClusterVersionZonalResponseBodyDBRevisionVersionList] = None,
        dbversion: str = None,
        dbversion_status: str = None,
        is_latest_version: str = None,
        is_proxy_latest_version: str = None,
        proxy_latest_version: str = None,
        proxy_revision_version: str = None,
        proxy_revision_version_list: List[main_models.DescribeDBClusterVersionZonalResponseBodyProxyRevisionVersionList] = None,
        proxy_version_status: str = None,
        request_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.dblatest_version = dblatest_version
        self.dbminor_version = dbminor_version
        self.dbrevision_version = dbrevision_version
        self.dbrevision_version_list = dbrevision_version_list
        self.dbversion = dbversion
        self.dbversion_status = dbversion_status
        self.is_latest_version = is_latest_version
        self.is_proxy_latest_version = is_proxy_latest_version
        self.proxy_latest_version = proxy_latest_version
        self.proxy_revision_version = proxy_revision_version
        self.proxy_revision_version_list = proxy_revision_version_list
        self.proxy_version_status = proxy_version_status
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

        if m.get('DBLatestVersion') is not None:
            self.dblatest_version = m.get('DBLatestVersion')

        if m.get('DBMinorVersion') is not None:
            self.dbminor_version = m.get('DBMinorVersion')

        if m.get('DBRevisionVersion') is not None:
            self.dbrevision_version = m.get('DBRevisionVersion')

        self.dbrevision_version_list = []
        if m.get('DBRevisionVersionList') is not None:
            for k1 in m.get('DBRevisionVersionList'):
                temp_model = main_models.DescribeDBClusterVersionZonalResponseBodyDBRevisionVersionList()
                self.dbrevision_version_list.append(temp_model.from_map(k1))

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('DBVersionStatus') is not None:
            self.dbversion_status = m.get('DBVersionStatus')

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
                temp_model = main_models.DescribeDBClusterVersionZonalResponseBodyProxyRevisionVersionList()
                self.proxy_revision_version_list.append(temp_model.from_map(k1))

        if m.get('ProxyVersionStatus') is not None:
            self.proxy_version_status = m.get('ProxyVersionStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBClusterVersionZonalResponseBodyProxyRevisionVersionList(DaraModel):
    def __init__(
        self,
        release_note: str = None,
        release_type: str = None,
        revision_version_code: str = None,
        revision_version_name: str = None,
    ):
        self.release_note = release_note
        self.release_type = release_type
        self.revision_version_code = revision_version_code
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

class DescribeDBClusterVersionZonalResponseBodyDBRevisionVersionList(DaraModel):
    def __init__(
        self,
        release_note: str = None,
        release_type: str = None,
        revision_version_code: str = None,
        revision_version_name: str = None,
    ):
        self.release_note = release_note
        self.release_type = release_type
        self.revision_version_code = revision_version_code
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

