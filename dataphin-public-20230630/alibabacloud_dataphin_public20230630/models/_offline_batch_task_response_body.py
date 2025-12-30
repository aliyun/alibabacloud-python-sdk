# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class OfflineBatchTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        offline_result: main_models.OfflineBatchTaskResponseBodyOfflineResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.offline_result = offline_result
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.offline_result:
            self.offline_result.validate()

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

        if self.offline_result is not None:
            result['OfflineResult'] = self.offline_result.to_map()

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

        if m.get('OfflineResult') is not None:
            temp_model = main_models.OfflineBatchTaskResponseBodyOfflineResult()
            self.offline_result = temp_model.from_map(m.get('OfflineResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class OfflineBatchTaskResponseBodyOfflineResult(DaraModel):
    def __init__(
        self,
        publish_object_id: int = None,
    ):
        self.publish_object_id = publish_object_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.publish_object_id is not None:
            result['PublishObjectId'] = self.publish_object_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PublishObjectId') is not None:
            self.publish_object_id = m.get('PublishObjectId')

        return self

