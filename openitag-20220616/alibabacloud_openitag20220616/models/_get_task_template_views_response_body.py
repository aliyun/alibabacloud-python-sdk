# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class GetTaskTemplateViewsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        views: main_models.GetTaskTemplateViewsResponseBodyViews = None,
    ):
        # Total amount of data under the current request conditions. This parameter is optional and does not need to be returned by default.
        self.code = code
        # Details
        self.details = details
        # error code
        self.error_code = error_code
        # Return message of the request
        # 
        # This parameter is required.
        self.message = message
        # Request ID
        self.request_id = request_id
        # is succeeded
        self.success = success
        # view
        self.views = views

    def validate(self):
        if self.views:
            self.views.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.details is not None:
            result['Details'] = self.details

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.views is not None:
            result['Views'] = self.views.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Details') is not None:
            self.details = m.get('Details')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Views') is not None:
            temp_model = main_models.GetTaskTemplateViewsResponseBodyViews()
            self.views = temp_model.from_map(m.get('Views'))

        return self

class GetTaskTemplateViewsResponseBodyViews(DaraModel):
    def __init__(
        self,
        view_plugins: List[main_models.ViewPlugin] = None,
    ):
        # List of view plugins
        self.view_plugins = view_plugins

    def validate(self):
        if self.view_plugins:
            for v1 in self.view_plugins:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ViewPlugins'] = []
        if self.view_plugins is not None:
            for k1 in self.view_plugins:
                result['ViewPlugins'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.view_plugins = []
        if m.get('ViewPlugins') is not None:
            for k1 in m.get('ViewPlugins'):
                temp_model = main_models.ViewPlugin()
                self.view_plugins.append(temp_model.from_map(k1))

        return self

