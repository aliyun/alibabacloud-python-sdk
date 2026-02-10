# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageFixCycleConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeImageFixCycleConfigResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeImageFixCycleConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageFixCycleConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        image_fix_cycle: int = None,
        image_fix_switch: str = None,
        image_fix_target: str = None,
        image_time_range: int = None,
    ):
        # The cycle of the scheduled fix. Unit: day.
        self.image_fix_cycle = image_fix_cycle
        # Indicates whether the scheduled fix of image risks is enabled.
        # 
        # *   **on**: enabled
        # *   **off**: disabled
        self.image_fix_switch = image_fix_switch
        # The range of the scheduled fix. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **type**: The type of the image risk. The value is fixed to repo.
        # *   **target**: The content of the image risk. The value is in the format of Namespace/Image repository.
        self.image_fix_target = image_fix_target
        # The time range during which the image was modified. Unit: day.
        self.image_time_range = image_time_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_fix_cycle is not None:
            result['ImageFixCycle'] = self.image_fix_cycle

        if self.image_fix_switch is not None:
            result['ImageFixSwitch'] = self.image_fix_switch

        if self.image_fix_target is not None:
            result['ImageFixTarget'] = self.image_fix_target

        if self.image_time_range is not None:
            result['ImageTimeRange'] = self.image_time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageFixCycle') is not None:
            self.image_fix_cycle = m.get('ImageFixCycle')

        if m.get('ImageFixSwitch') is not None:
            self.image_fix_switch = m.get('ImageFixSwitch')

        if m.get('ImageFixTarget') is not None:
            self.image_fix_target = m.get('ImageFixTarget')

        if m.get('ImageTimeRange') is not None:
            self.image_time_range = m.get('ImageTimeRange')

        return self

