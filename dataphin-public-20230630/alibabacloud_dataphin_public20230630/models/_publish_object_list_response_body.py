# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class PublishObjectListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        publish_result: main_models.PublishObjectListResponseBodyPublishResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.publish_result = publish_result
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.publish_result:
            self.publish_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.publish_result is not None:
            result['PublishResult'] = self.publish_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PublishResult') is not None:
            temp_model = main_models.PublishObjectListResponseBodyPublishResult()
            self.publish_result = temp_model.from_map(m.get('PublishResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class PublishObjectListResponseBodyPublishResult(DaraModel):
    def __init__(
        self,
        submit_id_list: List[int] = None,
    ):
        self.submit_id_list = submit_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.submit_id_list is not None:
            result['SubmitIdList'] = self.submit_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubmitIdList') is not None:
            self.submit_id_list = m.get('SubmitIdList')

        return self

