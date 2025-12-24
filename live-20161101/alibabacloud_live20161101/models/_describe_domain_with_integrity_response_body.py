# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainWithIntegrityResponseBody(DaraModel):
    def __init__(
        self,
        content: List[main_models.DescribeDomainWithIntegrityResponseBodyContent] = None,
        request_id: str = None,
    ):
        # The verification information.
        self.content = content
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.DescribeDomainWithIntegrityResponseBodyContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDomainWithIntegrityResponseBodyContent(DaraModel):
    def __init__(
        self,
        columns: List[str] = None,
        name: str = None,
        points: List[str] = None,
    ):
        # The column names.
        self.columns = columns
        # The table name.
        self.name = name
        # The subpoints.
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

