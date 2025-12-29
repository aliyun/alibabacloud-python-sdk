# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ListSortScriptsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListSortScriptsResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The scripts.
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
                temp_model = main_models.ListSortScriptsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListSortScriptsResponseBodyResult(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        scope: str = None,
        script_name: str = None,
        status: str = None,
        type: str = None,
    ):
        # The time when the script was created.
        self.create_time = create_time
        # The time when the script was last modified.
        self.modify_time = modify_time
        # The sort phase to which the script applies.
        self.scope = scope
        # The name of the script.
        self.script_name = script_name
        # The status of the script. Valid values:
        # 
        # *   configurable: The script is created, but no script files are uploaded.
        # *   not compiled: The script is not compiled.
        # *   compile failed: The compilation of the script failed.
        # *   compile successful: The script is compiled.
        # *   released: The script is published.
        self.status = status
        # The type of the script.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time

        if self.scope is not None:
            result['scope'] = self.scope

        if self.script_name is not None:
            result['scriptName'] = self.script_name

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

