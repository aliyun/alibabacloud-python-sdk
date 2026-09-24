# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class MerchandisePlacementDetectionProResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.MerchandisePlacementDetectionProResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The detection result of product display detection Pro.
        self.data = data
        # The response message or failure description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.MerchandisePlacementDetectionProResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class MerchandisePlacementDetectionProResponseBodyData(DaraModel):
    def __init__(
        self,
        box_count: int = None,
        data: List[main_models.MerchandisePlacementDetectionProResponseBodyDataData] = None,
        usage_map: Dict[str, int] = None,
    ):
        # The number of valid bounding boxes.
        self.box_count = box_count
        # The list of per-box detection details.
        self.data = data
        # The usage information.
        self.usage_map = usage_map

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.box_count is not None:
            result['BoxCount'] = self.box_count

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoxCount') is not None:
            self.box_count = m.get('BoxCount')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.MerchandisePlacementDetectionProResponseBodyDataData()
                self.data.append(temp_model.from_map(k1))

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

class MerchandisePlacementDetectionProResponseBodyDataData(DaraModel):
    def __init__(
        self,
        bbox_2d: List[int] = None,
        detected_sku_name: str = None,
        idx: int = None,
    ):
        # The normalized bounding box coordinates [x1,y1,x2,y2], with values in the range 0–1000.
        self.bbox_2d = bbox_2d
        # The detected product name. The value is unknown if the name cannot be determined.
        self.detected_sku_name = detected_sku_name
        # The bounding box index, starting from 1.
        self.idx = idx

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bbox_2d is not None:
            result['Bbox2d'] = self.bbox_2d

        if self.detected_sku_name is not None:
            result['DetectedSkuName'] = self.detected_sku_name

        if self.idx is not None:
            result['Idx'] = self.idx

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bbox2d') is not None:
            self.bbox_2d = m.get('Bbox2d')

        if m.get('DetectedSkuName') is not None:
            self.detected_sku_name = m.get('DetectedSkuName')

        if m.get('Idx') is not None:
            self.idx = m.get('Idx')

        return self

