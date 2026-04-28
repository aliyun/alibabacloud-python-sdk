# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class InvestigationInfo(DaraModel):
    def __init__(
        self,
        status: int = None,
        suggestion: str = None,
        video_detail: main_models.InvestigationInfoVideoDetail = None,
    ):
        # The status of the review.
        # 
        # Valid values:
        # 
        # *   0: The review is not performed.
        # *   1: The review is not supported.
        # *   2: The review fails.
        # *   3: The review is in progress.
        # *   4: The review is complete.
        # *   5: Penalty methods are applied.
        self.status = status
        # The recommended operation provided by the review.
        # 
        # Valid values:
        # 
        # *   pass: The review is passed..
        # *   block: The review is not passed. It is recommended to limit the use of the image.
        self.suggestion = suggestion
        # Video review information
        self.video_detail = video_detail

    def validate(self):
        if self.video_detail:
            self.video_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['status'] = self.status

        if self.suggestion is not None:
            result['suggestion'] = self.suggestion

        if self.video_detail is not None:
            result['video_detail'] = self.video_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('suggestion') is not None:
            self.suggestion = m.get('suggestion')

        if m.get('video_detail') is not None:
            temp_model = main_models.InvestigationInfoVideoDetail()
            self.video_detail = temp_model.from_map(m.get('video_detail'))

        return self

class InvestigationInfoVideoDetail(DaraModel):
    def __init__(
        self,
        block_frames: List[main_models.InvestigationInfoVideoDetailBlockFrames] = None,
    ):
        # Violation frame information
        self.block_frames = block_frames

    def validate(self):
        if self.block_frames:
            for v1 in self.block_frames:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['block_frames'] = []
        if self.block_frames is not None:
            for k1 in self.block_frames:
                result['block_frames'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.block_frames = []
        if m.get('block_frames') is not None:
            for k1 in m.get('block_frames'):
                temp_model = main_models.InvestigationInfoVideoDetailBlockFrames()
                self.block_frames.append(temp_model.from_map(k1))

        return self

class InvestigationInfoVideoDetailBlockFrames(DaraModel):
    def __init__(
        self,
        label: str = None,
        offset: int = None,
        rate: float = None,
    ):
        # Category of review results
        self.label = label
        # Time (in seconds)
        self.offset = offset
        # The confidence level. Valid values: 0 to 100.
        self.rate = rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['label'] = self.label

        if self.offset is not None:
            result['offset'] = self.offset

        if self.rate is not None:
            result['rate'] = self.rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('rate') is not None:
            self.rate = m.get('rate')

        return self

