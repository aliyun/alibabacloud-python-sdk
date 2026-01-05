# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeCrossCloudLevelsResponseBody(DaraModel):
    def __init__(
        self,
        cross_cloud_level_list: List[main_models.DescribeCrossCloudLevelsResponseBodyCrossCloudLevelList] = None,
        request_id: str = None,
    ):
        self.cross_cloud_level_list = cross_cloud_level_list
        self.request_id = request_id

    def validate(self):
        if self.cross_cloud_level_list:
            for v1 in self.cross_cloud_level_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CrossCloudLevelList'] = []
        if self.cross_cloud_level_list is not None:
            for k1 in self.cross_cloud_level_list:
                result['CrossCloudLevelList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cross_cloud_level_list = []
        if m.get('CrossCloudLevelList') is not None:
            for k1 in m.get('CrossCloudLevelList'):
                temp_model = main_models.DescribeCrossCloudLevelsResponseBodyCrossCloudLevelList()
                self.cross_cloud_level_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCrossCloudLevelsResponseBodyCrossCloudLevelList(DaraModel):
    def __init__(
        self,
        dbtype: str = None,
        level_code: str = None,
        level_name: str = None,
    ):
        self.dbtype = dbtype
        self.level_code = level_code
        self.level_name = level_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.level_code is not None:
            result['LevelCode'] = self.level_code

        if self.level_name is not None:
            result['LevelName'] = self.level_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('LevelCode') is not None:
            self.level_code = m.get('LevelCode')

        if m.get('LevelName') is not None:
            self.level_name = m.get('LevelName')

        return self

