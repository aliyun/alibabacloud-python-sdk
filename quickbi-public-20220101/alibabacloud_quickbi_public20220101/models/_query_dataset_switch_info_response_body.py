# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryDatasetSwitchInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryDatasetSwitchInfoResponseBodyResult = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the row- and column-level permission switches for the dataset.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # - true: The request is successful.
        # - false: The request fails.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryDatasetSwitchInfoResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryDatasetSwitchInfoResponseBodyResult(DaraModel):
    def __init__(
        self,
        cube_id: str = None,
        is_open_column_level_permission: int = None,
        is_open_row_level_permission: int = None,
    ):
        # The dataset ID.
        self.cube_id = cube_id
        # The status of the column-level field permission switch. Valid values:
        # 
        # - 1: Enabled.
        # - 0: Disabled.
        self.is_open_column_level_permission = is_open_column_level_permission
        # The status of the row-level permission switch. Valid values:
        # 
        # - 1: Enabled.
        # - 0: Disabled.
        self.is_open_row_level_permission = is_open_row_level_permission

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id

        if self.is_open_column_level_permission is not None:
            result['IsOpenColumnLevelPermission'] = self.is_open_column_level_permission

        if self.is_open_row_level_permission is not None:
            result['IsOpenRowLevelPermission'] = self.is_open_row_level_permission

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')

        if m.get('IsOpenColumnLevelPermission') is not None:
            self.is_open_column_level_permission = m.get('IsOpenColumnLevelPermission')

        if m.get('IsOpenRowLevelPermission') is not None:
            self.is_open_row_level_permission = m.get('IsOpenRowLevelPermission')

        return self

