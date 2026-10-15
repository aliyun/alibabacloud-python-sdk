# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class MerchandisePriceTagDetectionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.MerchandisePriceTagDetectionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The scenario recognition result.
        self.data = data
        # The return message or failure description.
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
            temp_model = main_models.MerchandisePriceTagDetectionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class MerchandisePriceTagDetectionResponseBodyData(DaraModel):
    def __init__(
        self,
        result: main_models.MerchandisePriceTagDetectionResponseBodyDataResult = None,
        usage_map: Dict[str, int] = None,
    ):
        # The detection and recognition result details.
        self.result = result
        # The usage information.
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
            temp_model = main_models.MerchandisePriceTagDetectionResponseBodyDataResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

class MerchandisePriceTagDetectionResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        grounding: main_models.MerchandisePriceTagDetectionResponseBodyDataResultGrounding = None,
        price_tags: List[main_models.MerchandisePriceTagDetectionResponseBodyDataResultPriceTags] = None,
        type: str = None,
    ):
        # The localization information.
        self.grounding = grounding
        # The price tag list. This can be an empty array if no price tags are recognized under normal conditions.
        self.price_tags = price_tags
        # The value is fixed to priceTag.
        self.type = type

    def validate(self):
        if self.grounding:
            self.grounding.validate()
        if self.price_tags:
            for v1 in self.price_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grounding is not None:
            result['Grounding'] = self.grounding.to_map()

        result['PriceTags'] = []
        if self.price_tags is not None:
            for k1 in self.price_tags:
                result['PriceTags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Grounding') is not None:
            temp_model = main_models.MerchandisePriceTagDetectionResponseBodyDataResultGrounding()
            self.grounding = temp_model.from_map(m.get('Grounding'))

        self.price_tags = []
        if m.get('PriceTags') is not None:
            for k1 in m.get('PriceTags'):
                temp_model = main_models.MerchandisePriceTagDetectionResponseBodyDataResultPriceTags()
                self.price_tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class MerchandisePriceTagDetectionResponseBodyDataResultPriceTags(DaraModel):
    def __init__(
        self,
        location: main_models.MerchandisePriceTagDetectionResponseBodyDataResultPriceTagsLocation = None,
        original_price: str = None,
        price: str = None,
        sku_code: str = None,
        sku_name: str = None,
    ):
        # The location.
        self.location = location
        # The original price.
        self.original_price = original_price
        # The selling price, retained as a string to avoid being parsed as a reserved word or reserved character.
        self.price = price
        # The associated product code.
        self.sku_code = sku_code
        # The associated product name.
        self.sku_name = sku_name

    def validate(self):
        if self.location:
            self.location.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.location is not None:
            result['Location'] = self.location.to_map()

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        if self.price is not None:
            result['Price'] = self.price

        if self.sku_code is not None:
            result['SkuCode'] = self.sku_code

        if self.sku_name is not None:
            result['SkuName'] = self.sku_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            temp_model = main_models.MerchandisePriceTagDetectionResponseBodyDataResultPriceTagsLocation()
            self.location = temp_model.from_map(m.get('Location'))

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('SkuCode') is not None:
            self.sku_code = m.get('SkuCode')

        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')

        return self

class MerchandisePriceTagDetectionResponseBodyDataResultPriceTagsLocation(DaraModel):
    def __init__(
        self,
        bottom: str = None,
        left: str = None,
        right: str = None,
        top: str = None,
    ):
        # The bottom boundary of the detection box.
        self.bottom = bottom
        # The left boundary of the detection box.
        self.left = left
        # The right boundary of the detection box.
        self.right = right
        # The top boundary of the detection box.
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
            result['top'] = self.top

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bottom') is not None:
            self.bottom = m.get('Bottom')

        if m.get('Left') is not None:
            self.left = m.get('Left')

        if m.get('Right') is not None:
            self.right = m.get('Right')

        if m.get('top') is not None:
            self.top = m.get('top')

        return self

class MerchandisePriceTagDetectionResponseBodyDataResultGrounding(DaraModel):
    def __init__(
        self,
        coverage: str = None,
        regions: List[main_models.MerchandisePriceTagDetectionResponseBodyDataResultGroundingRegions] = None,
    ):
        # The coverage.
        self.coverage = coverage
        # The region list.
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
                temp_model = main_models.MerchandisePriceTagDetectionResponseBodyDataResultGroundingRegions()
                self.regions.append(temp_model.from_map(k1))

        return self

class MerchandisePriceTagDetectionResponseBodyDataResultGroundingRegions(DaraModel):
    def __init__(
        self,
        bbox_2d: List[float] = None,
        label: str = None,
        text: str = None,
    ):
        # The bounding box coordinates.
        self.bbox_2d = bbox_2d
        # The label.
        self.label = label
        # The recognized text.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bbox_2d is not None:
            result['Bbox2d'] = self.bbox_2d

        if self.label is not None:
            result['Label'] = self.label

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bbox2d') is not None:
            self.bbox_2d = m.get('Bbox2d')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

