# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetAppPlayKeyResponseBody(DaraModel):
    def __init__(
        self,
        app_play_key: main_models.GetAppPlayKeyResponseBodyAppPlayKey = None,
        request_id: str = None,
    ):
        self.app_play_key = app_play_key
        self.request_id = request_id

    def validate(self):
        if self.app_play_key:
            self.app_play_key.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_play_key is not None:
            result['AppPlayKey'] = self.app_play_key.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppPlayKey') is not None:
            temp_model = main_models.GetAppPlayKeyResponseBodyAppPlayKey()
            self.app_play_key = temp_model.from_map(m.get('AppPlayKey'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAppPlayKeyResponseBodyAppPlayKey(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        creation_time: str = None,
        modification_time: str = None,
        play_key: str = None,
    ):
        self.app_id = app_id
        self.creation_time = creation_time
        self.modification_time = modification_time
        self.play_key = play_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.play_key is not None:
            result['PlayKey'] = self.play_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('PlayKey') is not None:
            self.play_key = m.get('PlayKey')

        return self

