# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeHighlightInfoResponseBody(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeHighlightInfoResponseBodyDataModule] = None,
        request_id: str = None,
    ):
        # The data model of the highlighted data.
        self.data_module = data_module
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data_module:
            for v1 in self.data_module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataModule'] = []
        if self.data_module is not None:
            for k1 in self.data_module:
                result['DataModule'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k1 in m.get('DataModule'):
                temp_model = main_models.DescribeHighlightInfoResponseBodyDataModule()
                self.data_module.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeHighlightInfoResponseBodyDataModule(DaraModel):
    def __init__(
        self,
        hit: str = None,
        key: str = None,
        raw: str = None,
    ):
        # The highlighted data.
        self.hit = hit
        # The type of the highlighted data.
        self.key = key
        # The complete data.
        self.raw = raw

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hit is not None:
            result['Hit'] = self.hit

        if self.key is not None:
            result['Key'] = self.key

        if self.raw is not None:
            result['Raw'] = self.raw

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hit') is not None:
            self.hit = m.get('Hit')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Raw') is not None:
            self.raw = m.get('Raw')

        return self

