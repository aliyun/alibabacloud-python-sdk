# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class ModifyCallbackMetaRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        callback: main_models.ModifyCallbackMetaRequestCallback = None,
        owner_id: int = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.callback = callback
        self.owner_id = owner_id

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

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Callback') is not None:
            temp_model = main_models.ModifyCallbackMetaRequestCallback()
            self.callback = temp_model.from_map(m.get('Callback'))

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

class ModifyCallbackMetaRequestCallback(DaraModel):
    def __init__(
        self,
        category: str = None,
        conf: str = None,
        sub_event: List[int] = None,
    ):
        # This parameter is required.
        self.category = category
        # This parameter is required.
        self.conf = conf
        self.sub_event = sub_event

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.conf is not None:
            result['Conf'] = self.conf

        if self.sub_event is not None:
            result['SubEvent'] = self.sub_event

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Conf') is not None:
            self.conf = m.get('Conf')

        if m.get('SubEvent') is not None:
            self.sub_event = m.get('SubEvent')

        return self

