# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class DiduiAreaDeductionRequest(DaraModel):
    def __init__(
        self,
        products: List[main_models.DiduiAreaDeductionRequestProducts] = None,
        rag_id: str = None,
        req_id: str = None,
        target_image_url: str = None,
    ):
        # The list of products and their detection boxes.
        # 
        # This parameter is required.
        self.products = products
        # The ID of the customer-specific SKU vector database that determines which database is used for retrieval. The database must be created in advance through the database creation process.
        self.rag_id = rag_id
        # The optional business request ID used for Tracing Analysis.
        self.req_id = req_id
        # The HTTPS URL of the overall floor display image.
        # 
        # This parameter is required.
        self.target_image_url = target_image_url

    def validate(self):
        if self.products:
            for v1 in self.products:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Products'] = []
        if self.products is not None:
            for k1 in self.products:
                result['Products'].append(k1.to_map() if k1 else None)

        if self.rag_id is not None:
            result['RagId'] = self.rag_id

        if self.req_id is not None:
            result['ReqId'] = self.req_id

        if self.target_image_url is not None:
            result['TargetImageUrl'] = self.target_image_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.products = []
        if m.get('Products') is not None:
            for k1 in m.get('Products'):
                temp_model = main_models.DiduiAreaDeductionRequestProducts()
                self.products.append(temp_model.from_map(k1))

        if m.get('RagId') is not None:
            self.rag_id = m.get('RagId')

        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')

        if m.get('TargetImageUrl') is not None:
            self.target_image_url = m.get('TargetImageUrl')

        return self

class DiduiAreaDeductionRequestProducts(DaraModel):
    def __init__(
        self,
        boxes: List[main_models.DiduiAreaDeductionRequestProductsBoxes] = None,
        sku_id: str = None,
    ):
        # The detection boxes for the current SKU. Coordinate values range from 0 to 1000.
        # 
        # This parameter is required.
        self.boxes = boxes
        # The unique ID of the SKU.
        # 
        # This parameter is required.
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
                temp_model = main_models.DiduiAreaDeductionRequestProductsBoxes()
                self.boxes.append(temp_model.from_map(k1))

        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')

        return self

class DiduiAreaDeductionRequestProductsBoxes(DaraModel):
    def __init__(
        self,
        bottom: float = None,
        left: float = None,
        right: float = None,
        top: float = None,
    ):
        # The bottom boundary of the detection box.
        # 
        # This parameter is required.
        self.bottom = bottom
        # The left boundary of the detection box.
        # 
        # This parameter is required.
        self.left = left
        # The right boundary of the detection box.
        # 
        # This parameter is required.
        self.right = right
        # The top boundary of the detection box.
        # 
        # This parameter is required.
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

