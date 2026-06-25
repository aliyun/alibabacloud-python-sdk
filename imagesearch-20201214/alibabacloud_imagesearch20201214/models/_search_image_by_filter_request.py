# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchImageByFilterRequest(DaraModel):
    def __init__(
        self,
        filter: str = None,
        instance_name: str = None,
        num: int = None,
        start: int = None,
    ):
        # The filter conditions. The operators supported by int_attr include in, not in, greater than (>), greater than or equal to (>=), less than (<), less than or equal to (<=), and equal to (=). The operators supported by str_attr include in, not in, equal to (=), and not equal to (!=). Multiple conditions can be connected by AND and OR.
        # Examples:
        # - int_attr >= 100.
        # - str_attr != "value1".
        # - int_attr = 1000 AND str_attr = "value1".
        # 
        # >A maximum of 4,096 characters are supported.
        # 
        # This parameter is required.
        self.filter = filter
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # If you have purchased an Image Search instance, you can log on to the [Image Search console](https://imagesearch.console.aliyun.com/) to view the instance.
        # If you have not purchased an Image Search instance, see [Activate the service](https://help.aliyun.com/document_detail/179178.html) and [Create an instance](https://help.aliyun.com/document_detail/66569.html).
        # >The instance name is not the instance ID. Make sure that you can distinguish between them.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The number of results to return. Valid values: 1 to 100. Default value: 10.
        self.num = num
        # The start position of the results to return. Valid values: 0 to 499. Default value: 0.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['Filter'] = self.filter

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.num is not None:
            result['Num'] = self.num

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Num') is not None:
            self.num = m.get('Num')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

