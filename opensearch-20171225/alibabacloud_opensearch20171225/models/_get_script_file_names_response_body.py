# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class GetScriptFileNamesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.GetScriptFileNamesResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The files of the script.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.GetScriptFileNamesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class GetScriptFileNamesResponseBodyResult(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        file_name: str = None,
        modify_time: str = None,
        path_name: str = None,
    ):
        # The time when the script file was created.
        self.create_time = create_time
        # The name of the script file.
        self.file_name = file_name
        # The time when the script file was last modified.
        self.modify_time = modify_time
        # The path name of the script file.
        self.path_name = path_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time

        if self.path_name is not None:
            result['pathName'] = self.path_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')

        if m.get('pathName') is not None:
            self.path_name = m.get('pathName')

        return self

