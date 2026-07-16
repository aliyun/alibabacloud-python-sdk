# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchImageByTextRequest(DaraModel):
    def __init__(
        self,
        distinct_product_id: bool = None,
        filter: str = None,
        instance_name: str = None,
        num: int = None,
        score_threshold: str = None,
        start: int = None,
        text: str = None,
    ):
        # If this parameter is set to true, duplicate data is removed based on the ProductId field during the search.
        self.distinct_product_id = distinct_product_id
        # The filter condition. The int_attr field supports the following operators: in, not in, greater than (>), greater than or equal to (>=), less than (<), less than or equal to (<=), and equal to (=). The str_attr field supports the following operators: in, not in, equal to (=), and not equal to (!=). You can use AND and OR to connect multiple conditions.
        # Examples:
        # - int_attr >= 100.
        # - str_attr != "value1".
        # - int_attr = 1000 AND str_attr = "value1".
        # 
        # >The filter condition can be up to 4,096 characters in length.
        self.filter = filter
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # If you have purchased an Image Search instance, log on to the [Image Search console](https://imagesearch.console.aliyun.com/) to view the instance name.
        # If you have not purchased an Image Search instance, see [Activate the service](https://help.aliyun.com/document_detail/179178.html) and [Create an instance](https://help.aliyun.com/document_detail/66569.html).
        # >The instance name is not the instance ID. Make sure you distinguish between them.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The number of results to return. Valid values: 1 to 100. Default value: 10.
        self.num = num
        # The similarity score threshold. After you specify this parameter, only images whose similarity scores are greater than or equal to the threshold are returned. Valid values: 0.00 to 1.00. The value supports up to two decimal places. Default value: 0.00.
        self.score_threshold = score_threshold
        # The start position of the results to return. Valid values: 0 to 499. Default value: 0.
        self.start = start
        # The description text for searching images. Chinese and English are supported.
        # 
        # >The text can be up to 512 characters in length.
        # 
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.distinct_product_id is not None:
            result['DistinctProductId'] = self.distinct_product_id

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.num is not None:
            result['Num'] = self.num

        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold

        if self.start is not None:
            result['Start'] = self.start

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistinctProductId') is not None:
            self.distinct_product_id = m.get('DistinctProductId')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Num') is not None:
            self.num = m.get('Num')

        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

