# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QuerySmartqPermissionByCubeIdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QuerySmartqPermissionByCubeIdResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Basic information of the dataset.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
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
            temp_model = main_models.QuerySmartqPermissionByCubeIdResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySmartqPermissionByCubeIdResponseBodyResult(DaraModel):
    def __init__(
        self,
        cube_id: str = None,
        cube_name: str = None,
        has_perssion: bool = None,
    ):
        # Dataset ID.
        self.cube_id = cube_id
        # Dataset name.
        self.cube_name = cube_name
        # Whether the current user has permission for the smart question. Note: \\"HasPerssion\\" seems to be a typo, it should probably be \\"HasPermission\\".
        self.has_perssion = has_perssion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id

        if self.cube_name is not None:
            result['CubeName'] = self.cube_name

        if self.has_perssion is not None:
            result['HasPerssion'] = self.has_perssion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')

        if m.get('CubeName') is not None:
            self.cube_name = m.get('CubeName')

        if m.get('HasPerssion') is not None:
            self.has_perssion = m.get('HasPerssion')

        return self

