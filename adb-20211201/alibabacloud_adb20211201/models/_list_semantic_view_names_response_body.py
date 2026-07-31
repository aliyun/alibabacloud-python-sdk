# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ListSemanticViewNamesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListSemanticViewNamesResponseBodyData] = None,
        request_id: str = None,
    ):
        # The returned result data.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListSemanticViewNamesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSemanticViewNamesResponseBodyData(DaraModel):
    def __init__(
        self,
        comment: str = None,
        view_name: str = None,
        view_schema: str = None,
    ):
        # The annotation of the semantic view.
        self.comment = comment
        # The name of the semantic view.
        self.view_name = view_name
        # The schema in which the semantic view resides.
        self.view_schema = view_schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.view_name is not None:
            result['ViewName'] = self.view_name

        if self.view_schema is not None:
            result['ViewSchema'] = self.view_schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('ViewName') is not None:
            self.view_name = m.get('ViewName')

        if m.get('ViewSchema') is not None:
            self.view_schema = m.get('ViewSchema')

        return self

