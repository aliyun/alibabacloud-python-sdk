# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DeleteAppLayoutRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        client_token: str = None,
        layout: main_models.DeleteAppLayoutRequestLayout = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.client_token = client_token
        self.layout = layout

    def validate(self):
        if self.layout:
            self.layout.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.layout is not None:
            result['Layout'] = self.layout.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Layout') is not None:
            temp_model = main_models.DeleteAppLayoutRequestLayout()
            self.layout = temp_model.from_map(m.get('Layout'))

        return self

class DeleteAppLayoutRequestLayout(DaraModel):
    def __init__(
        self,
        layout_id: str = None,
    ):
        # This parameter is required.
        self.layout_id = layout_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        return self

