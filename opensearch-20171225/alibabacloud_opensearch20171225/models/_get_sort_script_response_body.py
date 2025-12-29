# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class GetSortScriptResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetSortScriptResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the script.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.GetSortScriptResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class GetSortScriptResponseBodyResult(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        modify_time: str = None,
        scope: str = None,
        script_name: str = None,
        status: str = None,
        type: str = None,
    ):
        # The time when the script was created.
        self.create_time = create_time
        self.description = description
        # The time when the script was last modified.
        self.modify_time = modify_time
        # The sort phase to which the script applies.
        self.scope = scope
        # The name of the script.
        self.script_name = script_name
        # The status of the script. For more information, see the description of the status response parameter in the ListSortScripts topic.
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

        if self.description is not None:
            result['description'] = self.description

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

        if m.get('description') is not None:
            self.description = m.get('description')

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

