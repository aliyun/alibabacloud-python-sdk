# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class QuerySessionInfoResponseBody(DaraModel):
    def __init__(
        self,
        query_resource_info_list: List[main_models.QuerySessionInfoResponseBodyQueryResourceInfoList] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.query_resource_info_list = query_resource_info_list
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.query_resource_info_list:
            for v1 in self.query_resource_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['queryResourceInfoList'] = []
        if self.query_resource_info_list is not None:
            for k1 in self.query_resource_info_list:
                result['queryResourceInfoList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.query_resource_info_list = []
        if m.get('queryResourceInfoList') is not None:
            for k1 in m.get('queryResourceInfoList'):
                temp_model = main_models.QuerySessionInfoResponseBodyQueryResourceInfoList()
                self.query_resource_info_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class QuerySessionInfoResponseBodyQueryResourceInfoList(DaraModel):
    def __init__(
        self,
        session_id: str = None,
        status: str = None,
    ):
        self.session_id = session_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

