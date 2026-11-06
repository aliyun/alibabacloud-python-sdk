# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationAvailableVersionResponseBody(DaraModel):
    def __init__(
        self,
        latest_version: str = None,
        request_id: str = None,
        versions: List[main_models.DescribeApplicationAvailableVersionResponseBodyVersions] = None,
    ):
        # The latest version.
        self.latest_version = latest_version
        # The request ID.
        self.request_id = request_id
        # The list of versions.
        self.versions = versions

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
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['Versions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.versions = []
        if m.get('Versions') is not None:
            for k1 in m.get('Versions'):
                temp_model = main_models.DescribeApplicationAvailableVersionResponseBodyVersions()
                self.versions.append(temp_model.from_map(k1))

        return self

class DescribeApplicationAvailableVersionResponseBodyVersions(DaraModel):
    def __init__(
        self,
        release_date: str = None,
        release_note: str = None,
        release_type: str = None,
        version: str = None,
        version_description: str = None,
    ):
        # The release date.
        self.release_date = release_date
        # The release notes of the version.
        self.release_note = release_note
        # The release type.
        self.release_type = release_type
        # The version number.
        self.version = version
        # The version description.
        self.version_description = version_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.release_date is not None:
            result['ReleaseDate'] = self.release_date

        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note

        if self.release_type is not None:
            result['ReleaseType'] = self.release_type

        if self.version is not None:
            result['Version'] = self.version

        if self.version_description is not None:
            result['VersionDescription'] = self.version_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReleaseDate') is not None:
            self.release_date = m.get('ReleaseDate')

        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')

        if m.get('ReleaseType') is not None:
            self.release_type = m.get('ReleaseType')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')

        return self

