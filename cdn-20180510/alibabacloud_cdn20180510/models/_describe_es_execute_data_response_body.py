# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeEsExecuteDataResponseBody(DaraModel):
    def __init__(
        self,
        contents: List[main_models.DescribeEsExecuteDataResponseBodyContents] = None,
        request_id: str = None,
    ):
        # The content of the script.
        self.contents = contents
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.contents:
            for v1 in self.contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Contents'] = []
        if self.contents is not None:
            for k1 in self.contents:
                result['Contents'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contents = []
        if m.get('Contents') is not None:
            for k1 in m.get('Contents'):
                temp_model = main_models.DescribeEsExecuteDataResponseBodyContents()
                self.contents.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEsExecuteDataResponseBodyContents(DaraModel):
    def __init__(
        self,
        columns: List[str] = None,
        name: str = None,
        points: List[str] = None,
    ):
        # The time and column names in the table that shows the status of the script.
        self.columns = columns
        # The name of the table that shows the status of the script.
        self.name = name
        # The list of timestamps and values in the corresponding columns of the table that shows the status of the script.
        self.points = points

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columns is not None:
            result['Columns'] = self.columns

        if self.name is not None:
            result['Name'] = self.name

        if self.points is not None:
            result['Points'] = self.points

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Columns') is not None:
            self.columns = m.get('Columns')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Points') is not None:
            self.points = m.get('Points')

        return self

