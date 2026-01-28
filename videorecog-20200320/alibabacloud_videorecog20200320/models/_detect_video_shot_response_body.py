# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_videorecog20200320 import models as main_models
from darabonba.model import DaraModel

class DetectVideoShotResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DetectVideoShotResponseBodyData = None,
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
            temp_model = main_models.DetectVideoShotResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self



class DetectVideoShotResponseBodyData(DaraModel):
    def __init__(
        self,
        shot_frame_ids: List[int] = None,
    ):
        # 1
        self.shot_frame_ids = shot_frame_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.shot_frame_ids is not None:
            result['ShotFrameIds'] = self.shot_frame_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShotFrameIds') is not None:
            self.shot_frame_ids = m.get('ShotFrameIds')

        return self

