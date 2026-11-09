# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_onsmqtt20200420 import models as main_models
from darabonba.model import DaraModel

class DeleteWildcardByTopicResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DeleteWildcardByTopicResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. Valid values:
        # - 200: success.
        # - Other values: error codes. For more information, see error codes.
        self.code = code
        # The rule information dataset.
        self.data = data
        # Id of the request
        self.request_id = request_id
        # Indicates whether the operation was successful. Valid values:
        # - true: The operation was successful.
        # - false: The operation failed.
        self.success = success

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DeleteWildcardByTopicResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DeleteWildcardByTopicResponseBodyData(DaraModel):
    def __init__(
        self,
        deleted: str = None,
    ):
        # Indicates whether the deletion was successful. Valid values:
        # - **true**: The deletion was successful.
        # - **false**: The deletion failed.
        self.deleted = deleted

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deleted is not None:
            result['Deleted'] = self.deleted

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        return self

