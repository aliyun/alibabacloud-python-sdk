# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class GetAlertDestinationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAlertDestinationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        # - If `code == Success`, the authorization is successful.
        # - Other status codes indicate authorization failed. Check the `message` field for the detailed fault information.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        # - If `code == Success`, this field is empty.
        # - Otherwise, this field contains the request error information.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetAlertDestinationResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetAlertDestinationResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        id: int = None,
        name: str = None,
        params: Any = None,
        source: str = None,
        target: str = None,
        uid: str = None,
        updated_at: str = None,
    ):
        # The creation time.
        self.created_at = created_at
        # The alert contact ID.
        self.id = id
        # The alert contact name.
        self.name = name
        # The configuration parameters.
        self.params = params
        # The configuration source.
        self.source = source
        # The alert notification target. Currently, only DingTalk chatbots are supported.
        self.target = target
        # The user ID.
        self.uid = uid
        # The update time.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.params is not None:
            result['params'] = self.params

        if self.source is not None:
            result['source'] = self.source

        if self.target is not None:
            result['target'] = self.target

        if self.uid is not None:
            result['uid'] = self.uid

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('params') is not None:
            self.params = m.get('params')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('target') is not None:
            self.target = m.get('target')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

