# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class BatchQueryIndividuationTextResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        text_list: List[main_models.BatchQueryIndividuationTextResponseBodyTextList] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.text_list = text_list

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
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['textList'] = []
        if self.text_list is not None:
            for k1 in self.text_list:
                result['textList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.text_list = []
        if m.get('textList') is not None:
            for k1 in m.get('textList'):
                temp_model = main_models.BatchQueryIndividuationTextResponseBodyTextList()
                self.text_list.append(temp_model.from_map(k1))

        return self

class BatchQueryIndividuationTextResponseBodyTextList(DaraModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        error_msg: str = None,
        item_id: str = None,
        project_id: str = None,
        status: str = None,
        task_id: str = None,
        text_id: str = None,
        update_time: str = None,
        user_id: str = None,
    ):
        self.content = content
        self.create_time = create_time
        self.error_msg = error_msg
        self.item_id = item_id
        self.project_id = project_id
        self.status = status
        self.task_id = task_id
        self.text_id = text_id
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.item_id is not None:
            result['itemId'] = self.item_id

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.text_id is not None:
            result['textId'] = self.text_id

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('textId') is not None:
            self.text_id = m.get('textId')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

