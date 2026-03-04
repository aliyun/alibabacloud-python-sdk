# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MediaConvertSegment(DaraModel):
    def __init__(
        self,
        duration: int = None,
        force_seg_time: str = None,
    ):
        # The length of the segment.
        # 
        # *   Unit: seconds.
        # *   Valid values: [1,60].
        # *   Default value: 10. A value of 10 will create segments at the 10s, 20s, 30s, and 40s marks of the video.
        self.duration = duration
        # The points in time at which the video is forcibly segmented. Separate multiple points with commas (,). You can specify up to 10 points.
        # 
        # *   Format: {Point in time},{Point in time},{Point in time}.
        # *   Type: decimal. This parameter supports up to three decimal places.
        # *   Unit: seconds.
        # *   Example: 1,2,4,6,10,14,18, which specifies that the video is forcibly segmented at the 1st, 2nd, 4th, 6th, 10th, 14th, and 18th seconds.
        self.force_seg_time = force_seg_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.force_seg_time is not None:
            result['ForceSegTime'] = self.force_seg_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ForceSegTime') is not None:
            self.force_seg_time = m.get('ForceSegTime')

        return self

