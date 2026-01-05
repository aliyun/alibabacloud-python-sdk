# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBMiniEngineVersionsResponseBody(DaraModel):
    def __init__(
        self,
        dbrevision_version_list: List[main_models.DescribeDBMiniEngineVersionsResponseBodyDBRevisionVersionList] = None,
        request_id: str = None,
    ):
        self.dbrevision_version_list = dbrevision_version_list
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.dbrevision_version_list:
            for v1 in self.dbrevision_version_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBRevisionVersionList'] = []
        if self.dbrevision_version_list is not None:
            for k1 in self.dbrevision_version_list:
                result['DBRevisionVersionList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbrevision_version_list = []
        if m.get('DBRevisionVersionList') is not None:
            for k1 in m.get('DBRevisionVersionList'):
                temp_model = main_models.DescribeDBMiniEngineVersionsResponseBodyDBRevisionVersionList()
                self.dbrevision_version_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBMiniEngineVersionsResponseBodyDBRevisionVersionList(DaraModel):
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

