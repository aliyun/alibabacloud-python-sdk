# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeEnsNetLevelResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        ens_net_levels: main_models.DescribeEnsNetLevelResponseBodyEnsNetLevels = None,
        request_id: str = None,
    ):
        # The returned service code. A value of 0 indicates that the operation was successful.
        self.code = code
        # The network levels.
        self.ens_net_levels = ens_net_levels
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.ens_net_levels:
            self.ens_net_levels.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.ens_net_levels is not None:
            result['EnsNetLevels'] = self.ens_net_levels.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EnsNetLevels') is not None:
            temp_model = main_models.DescribeEnsNetLevelResponseBodyEnsNetLevels()
            self.ens_net_levels = temp_model.from_map(m.get('EnsNetLevels'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEnsNetLevelResponseBodyEnsNetLevels(DaraModel):
    def __init__(
        self,
        ens_net_level: List[main_models.DescribeEnsNetLevelResponseBodyEnsNetLevelsEnsNetLevel] = None,
    ):
        self.ens_net_level = ens_net_level

    def validate(self):
        if self.ens_net_level:
            for v1 in self.ens_net_level:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EnsNetLevel'] = []
        if self.ens_net_level is not None:
            for k1 in self.ens_net_level:
                result['EnsNetLevel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ens_net_level = []
        if m.get('EnsNetLevel') is not None:
            for k1 in m.get('EnsNetLevel'):
                temp_model = main_models.DescribeEnsNetLevelResponseBodyEnsNetLevelsEnsNetLevel()
                self.ens_net_level.append(temp_model.from_map(k1))

        return self

class DescribeEnsNetLevelResponseBodyEnsNetLevelsEnsNetLevel(DaraModel):
    def __init__(
        self,
        ens_net_level_code: str = None,
    ):
        # The network level. Valid values:
        # 
        # *   Big: greater area.
        # *   Middle: province.
        # *   Small: city.
        self.ens_net_level_code = ens_net_level_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_net_level_code is not None:
            result['EnsNetLevelCode'] = self.ens_net_level_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsNetLevelCode') is not None:
            self.ens_net_level_code = m.get('EnsNetLevelCode')

        return self

