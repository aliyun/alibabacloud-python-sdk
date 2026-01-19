# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudcallcenter20200701 import models as main_models
from darabonba.model import DaraModel

class CreateCorpNumberGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateCorpNumberGroupResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreateCorpNumberGroupResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateCorpNumberGroupResponseBodyData(DaraModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        description: str = None,
        number_count: str = None,
        number_group_id: str = None,
        number_group_name: str = None,
    ):
        self.aliyun_uid = aliyun_uid
        self.description = description
        self.number_count = number_count
        self.number_group_id = number_group_id
        self.number_group_name = number_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.description is not None:
            result['Description'] = self.description

        if self.number_count is not None:
            result['NumberCount'] = self.number_count

        if self.number_group_id is not None:
            result['NumberGroupId'] = self.number_group_id

        if self.number_group_name is not None:
            result['NumberGroupName'] = self.number_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NumberCount') is not None:
            self.number_count = m.get('NumberCount')

        if m.get('NumberGroupId') is not None:
            self.number_group_id = m.get('NumberGroupId')

        if m.get('NumberGroupName') is not None:
            self.number_group_name = m.get('NumberGroupName')

        return self

