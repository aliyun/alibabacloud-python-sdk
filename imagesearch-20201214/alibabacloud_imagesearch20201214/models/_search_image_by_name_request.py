# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchImageByNameRequest(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        distinct_product_id: bool = None,
        filter: str = None,
        instance_name: str = None,
        num: int = None,
        pic_name: str = None,
        product_id: str = None,
        score_threshold: str = None,
        start: int = None,
    ):
        # The category of the product. For more information, see [Category references](https://help.aliyun.com/document_detail/179184.html).
        # 
        # *   For product search: If a category is specified, the specified category prevails. If no category is specified, the system estimates and selects a category. The category selected by the system is included in the response.
        # *   For generic search: The parameter value is set to 88888888 regardless of whether a category is specified.
        self.category_id = category_id
        self.distinct_product_id = distinct_product_id
        # The filter conditions. int_attr supports the following operators: >, >=, <, <=, and =. str_attr supports the following operators: = and !=. You can set the logical operator between conditions to AND or OR.
        # 
        # Examples:
        # 
        # *   int_attr>=100
        # *   str_attr!="value1"
        # *   int_attr=1000 AND str_attr="value1"
        self.filter = filter
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The number of images to return on each page. Valid values: 1 to 100. Default value: 10.
        self.num = num
        # The name of the image.
        # 
        # This parameter is required.
        self.pic_name = pic_name
        # The ID of the product.
        # 
        # This parameter is required.
        self.product_id = product_id
        self.score_threshold = score_threshold
        # The number of the image to return. Valid values: 0 to 499. Default value: 0.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.distinct_product_id is not None:
            result['DistinctProductId'] = self.distinct_product_id

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.num is not None:
            result['Num'] = self.num

        if self.pic_name is not None:
            result['PicName'] = self.pic_name

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('DistinctProductId') is not None:
            self.distinct_product_id = m.get('DistinctProductId')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Num') is not None:
            self.num = m.get('Num')

        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

