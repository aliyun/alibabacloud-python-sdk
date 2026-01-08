# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeOutgoingTagResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tag_list: List[main_models.DescribeOutgoingTagResponseBodyTagList] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.tag_list = tag_list
        self.total_count = total_count

    def validate(self):
        if self.tag_list:
            for v1 in self.tag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TagList'] = []
        if self.tag_list is not None:
            for k1 in self.tag_list:
                result['TagList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tag_list = []
        if m.get('TagList') is not None:
            for k1 in m.get('TagList'):
                temp_model = main_models.DescribeOutgoingTagResponseBodyTagList()
                self.tag_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeOutgoingTagResponseBodyTagList(DaraModel):
    def __init__(
        self,
        class_id: str = None,
        risk_level: int = None,
        tag_describe: str = None,
        tag_id: str = None,
        tag_name: str = None,
    ):
        self.class_id = class_id
        self.risk_level = risk_level
        self.tag_describe = tag_describe
        self.tag_id = tag_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_id is not None:
            result['ClassId'] = self.class_id

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.tag_describe is not None:
            result['TagDescribe'] = self.tag_describe

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('TagDescribe') is not None:
            self.tag_describe = m.get('TagDescribe')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

