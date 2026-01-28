# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_videorecog20200320 import models as main_models
from darabonba.model import DaraModel

class UnderstandVideoContentResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.UnderstandVideoContentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.UnderstandVideoContentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UnderstandVideoContentResponseBodyData(DaraModel):
    def __init__(
        self,
        tag_info: Dict[str, Any] = None,
        video_info: main_models.UnderstandVideoContentResponseBodyDataVideoInfo = None,
    ):
        self.tag_info = tag_info
        self.video_info = video_info

    def validate(self):
        if self.video_info:
            self.video_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_info is not None:
            result['TagInfo'] = self.tag_info

        if self.video_info is not None:
            result['VideoInfo'] = self.video_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagInfo') is not None:
            self.tag_info = m.get('TagInfo')

        if m.get('VideoInfo') is not None:
            temp_model = main_models.UnderstandVideoContentResponseBodyDataVideoInfo()
            self.video_info = temp_model.from_map(m.get('VideoInfo'))

        return self

class UnderstandVideoContentResponseBodyDataVideoInfo(DaraModel):
    def __init__(
        self,
        duration: int = None,
        fps: float = None,
        height: int = None,
        width: int = None,
    ):
        self.duration = duration
        self.fps = fps
        self.height = height
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.height is not None:
            result['Height'] = self.height

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

