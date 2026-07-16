# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class DescribeRuleMetadataResponseBody(DaraModel):
    def __init__(
        self,
        datas: List[main_models.DescribeRuleMetadataResponseBodyDatas] = None,
        request_id: str = None,
    ):
        # The list of metadata.
        self.datas = datas
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.datas:
            for v1 in self.datas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Datas'] = []
        if self.datas is not None:
            for k1 in self.datas:
                result['Datas'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.datas = []
        if m.get('Datas') is not None:
            for k1 in m.get('Datas'):
                temp_model = main_models.DescribeRuleMetadataResponseBodyDatas()
                self.datas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRuleMetadataResponseBodyDatas(DaraModel):
    def __init__(
        self,
        children: List[main_models.DescribeRuleMetadataResponseBodyDatasChildren] = None,
        text: str = None,
        value: str = None,
    ):
        # The subset of metadata.
        self.children = children
        # The human-readable content.
        self.text = text
        # The value.
        self.value = value

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.text is not None:
            result['Text'] = self.text

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.DescribeRuleMetadataResponseBodyDatasChildren()
                self.children.append(temp_model.from_map(k1))

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeRuleMetadataResponseBodyDatasChildren(DaraModel):
    def __init__(
        self,
        text: str = None,
        value: str = None,
    ):
        # The human-readable content.
        self.text = text
        # The value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['Text'] = self.text

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

