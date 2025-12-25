# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class CreatePluginAttachmentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreatePluginAttachmentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The response message returned.
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
            temp_model = main_models.CreatePluginAttachmentResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CreatePluginAttachmentResponseBodyData(DaraModel):
    def __init__(
        self,
        plugin_attachment_id: str = None,
    ):
        # The plug-in ID.
        self.plugin_attachment_id = plugin_attachment_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.plugin_attachment_id is not None:
            result['pluginAttachmentId'] = self.plugin_attachment_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pluginAttachmentId') is not None:
            self.plugin_attachment_id = m.get('pluginAttachmentId')

        return self

