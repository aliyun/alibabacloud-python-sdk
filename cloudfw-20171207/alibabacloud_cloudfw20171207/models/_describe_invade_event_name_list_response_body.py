# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeInvadeEventNameListResponseBody(DaraModel):
    def __init__(
        self,
        event_name_list: List[main_models.DescribeInvadeEventNameListResponseBodyEventNameList] = None,
        name_list: List[str] = None,
        request_id: str = None,
    ):
        self.event_name_list = event_name_list
        self.name_list = name_list
        self.request_id = request_id

    def validate(self):
        if self.event_name_list:
            for v1 in self.event_name_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventNameList'] = []
        if self.event_name_list is not None:
            for k1 in self.event_name_list:
                result['EventNameList'].append(k1.to_map() if k1 else None)

        if self.name_list is not None:
            result['NameList'] = self.name_list

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_name_list = []
        if m.get('EventNameList') is not None:
            for k1 in m.get('EventNameList'):
                temp_model = main_models.DescribeInvadeEventNameListResponseBodyEventNameList()
                self.event_name_list.append(temp_model.from_map(k1))

        if m.get('NameList') is not None:
            self.name_list = m.get('NameList')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInvadeEventNameListResponseBodyEventNameList(DaraModel):
    def __init__(
        self,
        event_key: str = None,
        event_name: str = None,
    ):
        self.event_key = event_key
        self.event_name = event_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_key is not None:
            result['EventKey'] = self.event_key

        if self.event_name is not None:
            result['EventName'] = self.event_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventKey') is not None:
            self.event_key = m.get('EventKey')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        return self

