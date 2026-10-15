# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class MerchandisePlacementDetectionLiteResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.MerchandisePlacementDetectionLiteResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The returned result.
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
            temp_model = main_models.MerchandisePlacementDetectionLiteResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class MerchandisePlacementDetectionLiteResponseBodyData(DaraModel):
    def __init__(
        self,
        result: main_models.MerchandisePlacementDetectionLiteResponseBodyDataResult = None,
        usage_map: Dict[str, int] = None,
    ):
        # The result.
        self.result = result
        # The usage map. The value is {"ProcessingCount":1} for a successful call, and an empty object for a failed call.
        self.usage_map = usage_map

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            temp_model = main_models.MerchandisePlacementDetectionLiteResponseBodyDataResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

class MerchandisePlacementDetectionLiteResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        grounding: main_models.MerchandisePlacementDetectionLiteResponseBodyDataResultGrounding = None,
        products: List[main_models.MerchandisePlacementDetectionLiteResponseBodyDataResultProducts] = None,
        sku_ids: List[str] = None,
        type: str = None,
    ):
        # The supplementary element grounding results.
        self.grounding = grounding
        # The product items.
        self.products = products
        # The deduplicated list of SkuIds.
        self.sku_ids = sku_ids
        # The result type, which is fixed to sku.
        self.type = type

    def validate(self):
        if self.grounding:
            self.grounding.validate()
        if self.products:
            for v1 in self.products:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grounding is not None:
            result['Grounding'] = self.grounding.to_map()

        result['Products'] = []
        if self.products is not None:
            for k1 in self.products:
                result['Products'].append(k1.to_map() if k1 else None)

        if self.sku_ids is not None:
            result['SkuIds'] = self.sku_ids

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Grounding') is not None:
            temp_model = main_models.MerchandisePlacementDetectionLiteResponseBodyDataResultGrounding()
            self.grounding = temp_model.from_map(m.get('Grounding'))

        self.products = []
        if m.get('Products') is not None:
            for k1 in m.get('Products'):
                temp_model = main_models.MerchandisePlacementDetectionLiteResponseBodyDataResultProducts()
                self.products.append(temp_model.from_map(k1))

        if m.get('SkuIds') is not None:
            self.sku_ids = m.get('SkuIds')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class MerchandisePlacementDetectionLiteResponseBodyDataResultProducts(DaraModel):
    def __init__(
        self,
        boxes: List[main_models.MerchandisePlacementDetectionLiteResponseBodyDataResultProductsBoxes] = None,
        sku_id: str = None,
    ):
        # The bounding boxes corresponding to the SKU.
        self.boxes = boxes
        # The recognition code, which is obtained by removing the trailing _ce from the recognition name.
        self.sku_id = sku_id

    def validate(self):
        if self.boxes:
            for v1 in self.boxes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Boxes'] = []
        if self.boxes is not None:
            for k1 in self.boxes:
                result['Boxes'].append(k1.to_map() if k1 else None)

        if self.sku_id is not None:
            result['SkuId'] = self.sku_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.boxes = []
        if m.get('Boxes') is not None:
            for k1 in m.get('Boxes'):
                temp_model = main_models.MerchandisePlacementDetectionLiteResponseBodyDataResultProductsBoxes()
                self.boxes.append(temp_model.from_map(k1))

        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')

        return self

class MerchandisePlacementDetectionLiteResponseBodyDataResultProductsBoxes(DaraModel):
    def __init__(
        self,
        bottom: int = None,
        left: int = None,
        right: int = None,
        top: int = None,
    ):
        # The bottom coordinate.
        self.bottom = bottom
        # The left coordinate.
        self.left = left
        # The right coordinate.
        self.right = right
        # The bottom coordinate.
        self.top = top

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bottom is not None:
            result['Bottom'] = self.bottom

        if self.left is not None:
            result['Left'] = self.left

        if self.right is not None:
            result['Right'] = self.right

        if self.top is not None:
            result['Top'] = self.top

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bottom') is not None:
            self.bottom = m.get('Bottom')

        if m.get('Left') is not None:
            self.left = m.get('Left')

        if m.get('Right') is not None:
            self.right = m.get('Right')

        if m.get('Top') is not None:
            self.top = m.get('Top')

        return self

class MerchandisePlacementDetectionLiteResponseBodyDataResultGrounding(DaraModel):
    def __init__(
        self,
        coverage: str = None,
        regions: List[main_models.MerchandisePlacementDetectionLiteResponseBodyDataResultGroundingRegions] = None,
    ):
        # The coverage status. Valid values:
        # - complete: The relevant visible targets are complete.
        # - partial: Only some targets are valid or recognizable.
        # - Empty string: No valid supplementary grounding results are obtained.
        self.coverage = coverage
        # The target array, which contains up to 12 items. This array can be empty when no relevant targets are found.
        self.regions = regions

    def validate(self):
        if self.regions:
            for v1 in self.regions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coverage is not None:
            result['Coverage'] = self.coverage

        result['Regions'] = []
        if self.regions is not None:
            for k1 in self.regions:
                result['Regions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')

        self.regions = []
        if m.get('Regions') is not None:
            for k1 in m.get('Regions'):
                temp_model = main_models.MerchandisePlacementDetectionLiteResponseBodyDataResultGroundingRegions()
                self.regions.append(temp_model.from_map(k1))

        return self

class MerchandisePlacementDetectionLiteResponseBodyDataResultGroundingRegions(DaraModel):
    def __init__(
        self,
        bbox_2d: List[int] = None,
        label: str = None,
        text: str = None,
    ):
        # The 2D bounding box in the format of [top-left x, top-left y, bottom-right x, bottom-right y]. The values range from 0 to 1000. The left coordinate is less than the right coordinate, and the top coordinate is less than the bottom coordinate.
        self.bbox_2d = bbox_2d
        # The target category.
        self.label = label
        # The confirmable short name or text of up to 24 characters. This field is an empty string when the text is unclear.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bbox_2d is not None:
            result['Bbox_2d'] = self.bbox_2d

        if self.label is not None:
            result['Label'] = self.label

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bbox_2d') is not None:
            self.bbox_2d = m.get('Bbox_2d')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

