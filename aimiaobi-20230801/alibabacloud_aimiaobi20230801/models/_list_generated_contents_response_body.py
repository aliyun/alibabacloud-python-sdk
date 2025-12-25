# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListGeneratedContentsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: List[main_models.ListGeneratedContentsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.current = current
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.size = size
        self.success = success
        self.total = total

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
        if self.code is not None:
            result['Code'] = self.code

        if self.current is not None:
            result['Current'] = self.current

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.size is not None:
            result['Size'] = self.size

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListGeneratedContentsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListGeneratedContentsResponseBodyData(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_domain: str = None,
        content_text: str = None,
        create_time: str = None,
        create_user: str = None,
        device_id: str = None,
        file_attr: main_models.ListGeneratedContentsResponseBodyDataFileAttr = None,
        file_key: str = None,
        id: int = None,
        keyword_list: List[str] = None,
        keywords: str = None,
        prompt: str = None,
        task_id: str = None,
        title: str = None,
        update_time: str = None,
        update_user: str = None,
        uuid: str = None,
    ):
        self.content = content
        self.content_domain = content_domain
        self.content_text = content_text
        self.create_time = create_time
        self.create_user = create_user
        self.device_id = device_id
        self.file_attr = file_attr
        self.file_key = file_key
        self.id = id
        self.keyword_list = keyword_list
        self.keywords = keywords
        self.prompt = prompt
        self.task_id = task_id
        self.title = title
        self.update_time = update_time
        self.update_user = update_user
        self.uuid = uuid

    def validate(self):
        if self.file_attr:
            self.file_attr.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_domain is not None:
            result['ContentDomain'] = self.content_domain

        if self.content_text is not None:
            result['ContentText'] = self.content_text

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.file_attr is not None:
            result['FileAttr'] = self.file_attr.to_map()

        if self.file_key is not None:
            result['FileKey'] = self.file_key

        if self.id is not None:
            result['Id'] = self.id

        if self.keyword_list is not None:
            result['KeywordList'] = self.keyword_list

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.title is not None:
            result['Title'] = self.title

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_user is not None:
            result['UpdateUser'] = self.update_user

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentDomain') is not None:
            self.content_domain = m.get('ContentDomain')

        if m.get('ContentText') is not None:
            self.content_text = m.get('ContentText')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('FileAttr') is not None:
            temp_model = main_models.ListGeneratedContentsResponseBodyDataFileAttr()
            self.file_attr = temp_model.from_map(m.get('FileAttr'))

        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('KeywordList') is not None:
            self.keyword_list = m.get('KeywordList')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class ListGeneratedContentsResponseBodyDataFileAttr(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        height: int = None,
        tmp_url: str = None,
        width: int = None,
    ):
        self.file_name = file_name
        self.height = height
        self.tmp_url = tmp_url
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.height is not None:
            result['Height'] = self.height

        if self.tmp_url is not None:
            result['TmpUrl'] = self.tmp_url

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('TmpUrl') is not None:
            self.tmp_url = m.get('TmpUrl')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

