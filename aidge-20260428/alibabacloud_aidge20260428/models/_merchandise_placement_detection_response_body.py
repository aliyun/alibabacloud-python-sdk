# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class MerchandisePlacementDetectionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.MerchandisePlacementDetectionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. This parameter is not returned if the call is successful.
        self.code = code
        # The display detection result.
        self.data = data
        # The error message. This parameter is not returned if the call is successful.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # - true: The call is successful.
        # - false: The call failed.
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
            temp_model = main_models.MerchandisePlacementDetectionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class MerchandisePlacementDetectionResponseBodyData(DaraModel):
    def __init__(
        self,
        box_count: int = None,
        data: List[main_models.MerchandisePlacementDetectionResponseBodyDataData] = None,
        usage_map: Dict[str, int] = None,
    ):
        # The number of valid detection boxes.
        self.box_count = box_count
        # The list of retrieval details for each detection box.
        self.data = data
        # The usage information. The key is the usage metric name, and the value is the count.
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
                temp_model = main_models.MerchandisePlacementDetectionResponseBodyDataData()
                self.data.append(temp_model.from_map(k1))

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

class MerchandisePlacementDetectionResponseBodyDataData(DaraModel):
    def __init__(
        self,
        bbox: List[float] = None,
        error: str = None,
        idx: int = None,
        top_1: main_models.MerchandisePlacementDetectionResponseBodyDataDataTop1 = None,
        topk: List[main_models.MerchandisePlacementDetectionResponseBodyDataDataTopk] = None,
    ):
        # The position coordinates of the detection box in the format [x1,y1,x2,y2].
        self.bbox = bbox
        # The failure reason for the detection box. The value is null if the detection is successful.
        self.error = error
        # The index of the detection box.
        self.idx = idx
        # The top-1 recalled product for the detection box.
        self.top_1 = top_1
        # The list of top-K recalled products for the detection box.
        self.topk = topk

    def validate(self):
        if self.top_1:
            self.top_1.validate()
        if self.topk:
            for v1 in self.topk:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bbox is not None:
            result['Bbox'] = self.bbox

        if self.error is not None:
            result['Error'] = self.error

        if self.idx is not None:
            result['Idx'] = self.idx

        if self.top_1 is not None:
            result['Top1'] = self.top_1.to_map()

        result['Topk'] = []
        if self.topk is not None:
            for k1 in self.topk:
                result['Topk'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Idx') is not None:
            self.idx = m.get('Idx')

        if m.get('Top1') is not None:
            temp_model = main_models.MerchandisePlacementDetectionResponseBodyDataDataTop1()
            self.top_1 = temp_model.from_map(m.get('Top1'))

        self.topk = []
        if m.get('Topk') is not None:
            for k1 in m.get('Topk'):
                temp_model = main_models.MerchandisePlacementDetectionResponseBodyDataDataTopk()
                self.topk.append(temp_model.from_map(k1))

        return self

class MerchandisePlacementDetectionResponseBodyDataDataTopk(DaraModel):
    def __init__(
        self,
        rank: int = None,
        score: float = None,
        sku_id: str = None,
        sku_name: str = None,
    ):
        # The recall rank.
        self.rank = rank
        # The similarity score, ranging from 0 to 1.
        self.score = score
        # The ID of the recalled product.
        self.sku_id = sku_id
        # The name of the recalled product.
        self.sku_name = sku_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rank is not None:
            result['Rank'] = self.rank

        if self.score is not None:
            result['Score'] = self.score

        if self.sku_id is not None:
            result['SkuId'] = self.sku_id

        if self.sku_name is not None:
            result['SkuName'] = self.sku_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')

        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')

        return self

class MerchandisePlacementDetectionResponseBodyDataDataTop1(DaraModel):
    def __init__(
        self,
        score: float = None,
        sku_id: str = None,
        sku_name: str = None,
    ):
        # The similarity score, ranging from 0 to 1.
        self.score = score
        # The ID of the recalled product.
        self.sku_id = sku_id
        # The name of the recalled product.
        self.sku_name = sku_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.score is not None:
            result['Score'] = self.score

        if self.sku_id is not None:
            result['SkuId'] = self.sku_id

        if self.sku_name is not None:
            result['SkuName'] = self.sku_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')

        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')

        return self

