# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, BinaryIO

from alibabacloud_videorecog20200320 import models as main_models
from darabonba.model import DaraModel

class RecognizeVideoCastCrewListAdvanceRequest(DaraModel):
    def __init__(
        self,
        params: List[main_models.RecognizeVideoCastCrewListAdvanceRequestParams] = None,
        video_url_object: BinaryIO = None,
    ):
        self.params = params
        # This parameter is required.
        self.video_url_object = video_url_object

    def validate(self):
        if self.params:
            for v1 in self.params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Params'] = []
        if self.params is not None:
            for k1 in self.params:
                result['Params'].append(k1.to_map() if k1 else None)

        if self.video_url_object is not None:
            result['VideoUrl'] = self.video_url_object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.params = []
        if m.get('Params') is not None:
            for k1 in m.get('Params'):
                temp_model = main_models.RecognizeVideoCastCrewListAdvanceRequestParams()
                self.params.append(temp_model.from_map(k1))

        if m.get('VideoUrl') is not None:
            self.video_url_object = m.get('VideoUrl')

        return self

class RecognizeVideoCastCrewListAdvanceRequestParams(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

