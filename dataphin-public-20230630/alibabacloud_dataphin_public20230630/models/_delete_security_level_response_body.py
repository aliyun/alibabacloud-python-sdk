# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class DeleteSecurityLevelResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        delete_result: main_models.DeleteSecurityLevelResponseBodyDeleteResult = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.delete_result = delete_result
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.delete_result:
            self.delete_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.delete_result is not None:
            result['DeleteResult'] = self.delete_result.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DeleteResult') is not None:
            temp_model = main_models.DeleteSecurityLevelResponseBodyDeleteResult()
            self.delete_result = temp_model.from_map(m.get('DeleteResult'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DeleteSecurityLevelResponseBodyDeleteResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        related_classify_id_list: List[int] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.related_classify_id_list = related_classify_id_list
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.related_classify_id_list is not None:
            result['RelatedClassifyIdList'] = self.related_classify_id_list

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('RelatedClassifyIdList') is not None:
            self.related_classify_id_list = m.get('RelatedClassifyIdList')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

