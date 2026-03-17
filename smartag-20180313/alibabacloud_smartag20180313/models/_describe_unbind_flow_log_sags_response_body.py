# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeUnbindFlowLogSagsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        request_id: str = None,
        sags: main_models.DescribeUnbindFlowLogSagsResponseBodySags = None,
    ):
        # The total number of the SAG instances.
        self.count = count
        # The ID of the request.
        self.request_id = request_id
        self.sags = sags

    def validate(self):
        if self.sags:
            self.sags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sags is not None:
            result['Sags'] = self.sags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Sags') is not None:
            temp_model = main_models.DescribeUnbindFlowLogSagsResponseBodySags()
            self.sags = temp_model.from_map(m.get('Sags'))

        return self

class DescribeUnbindFlowLogSagsResponseBodySags(DaraModel):
    def __init__(
        self,
        sag: List[main_models.DescribeUnbindFlowLogSagsResponseBodySagsSag] = None,
    ):
        self.sag = sag

    def validate(self):
        if self.sag:
            for v1 in self.sag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Sag'] = []
        if self.sag is not None:
            for k1 in self.sag:
                result['Sag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sag = []
        if m.get('Sag') is not None:
            for k1 in m.get('Sag'):
                temp_model = main_models.DescribeUnbindFlowLogSagsResponseBodySagsSag()
                self.sag.append(temp_model.from_map(k1))

        return self

class DescribeUnbindFlowLogSagsResponseBodySagsSag(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        smart_agid: str = None,
    ):
        self.description = description
        self.name = name
        self.smart_agid = smart_agid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        return self

