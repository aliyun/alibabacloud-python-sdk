# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class StartCategoryCallbackRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        callback: main_models.StartCategoryCallbackRequestCallback = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.callback = callback

    def validate(self):
        if self.callback:
            self.callback.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.callback is not None:
            result['Callback'] = self.callback.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Callback') is not None:
            temp_model = main_models.StartCategoryCallbackRequestCallback()
            self.callback = temp_model.from_map(m.get('Callback'))

        return self

class StartCategoryCallbackRequestCallback(DaraModel):
    def __init__(
        self,
        category: str = None,
    ):
        # This parameter is required.
        self.category = category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        return self

