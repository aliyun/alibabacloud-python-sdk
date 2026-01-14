# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class QueryIndividuationTextTaskResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        request_id: str = None,
        status: int = None,
        text_list: List[main_models.QueryIndividuationTextTaskResponseBodyTextList] = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.text_list = text_list
        self.update_time = update_time

    def validate(self):
        if self.text_list:
            for v1 in self.text_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        result['textList'] = []
        if self.text_list is not None:
            for k1 in self.text_list:
                result['textList'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.text_list = []
        if m.get('textList') is not None:
            for k1 in m.get('textList'):
                temp_model = main_models.QueryIndividuationTextTaskResponseBodyTextList()
                self.text_list.append(temp_model.from_map(k1))

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class QueryIndividuationTextTaskResponseBodyTextList(DaraModel):
    def __init__(
        self,
        status: int = None,
        text_id: str = None,
        user_id: str = None,
    ):
        self.status = status
        self.text_id = text_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['status'] = self.status

        if self.text_id is not None:
            result['textId'] = self.text_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('textId') is not None:
            self.text_id = m.get('textId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

