# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class CreateOrUpdateSwimmingLaneGroupResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateOrUpdateSwimmingLaneGroupResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response parameters.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # true: The request was successful. false: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CreateOrUpdateSwimmingLaneGroupResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateOrUpdateSwimmingLaneGroupResponseBodyData(DaraModel):
    def __init__(
        self,
        app_ids: str = None,
        canary_model: int = None,
        db_gray_enable: str = None,
        entry_app: str = None,
        id: int = None,
        message_queue_filter_side: str = None,
        message_queue_gray_enable: bool = None,
        name: str = None,
        namespace: str = None,
        paths: str = None,
        record_canary_detail: bool = None,
        region: str = None,
        user_id: str = None,
    ):
        self.app_ids = app_ids
        self.canary_model = canary_model
        self.db_gray_enable = db_gray_enable
        self.entry_app = entry_app
        self.id = id
        self.message_queue_filter_side = message_queue_filter_side
        self.message_queue_gray_enable = message_queue_gray_enable
        self.name = name
        self.namespace = namespace
        self.paths = paths
        self.record_canary_detail = record_canary_detail
        self.region = region
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids

        if self.canary_model is not None:
            result['CanaryModel'] = self.canary_model

        if self.db_gray_enable is not None:
            result['DbGrayEnable'] = self.db_gray_enable

        if self.entry_app is not None:
            result['EntryApp'] = self.entry_app

        if self.id is not None:
            result['Id'] = self.id

        if self.message_queue_filter_side is not None:
            result['MessageQueueFilterSide'] = self.message_queue_filter_side

        if self.message_queue_gray_enable is not None:
            result['MessageQueueGrayEnable'] = self.message_queue_gray_enable

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.paths is not None:
            result['Paths'] = self.paths

        if self.record_canary_detail is not None:
            result['RecordCanaryDetail'] = self.record_canary_detail

        if self.region is not None:
            result['Region'] = self.region

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')

        if m.get('CanaryModel') is not None:
            self.canary_model = m.get('CanaryModel')

        if m.get('DbGrayEnable') is not None:
            self.db_gray_enable = m.get('DbGrayEnable')

        if m.get('EntryApp') is not None:
            self.entry_app = m.get('EntryApp')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MessageQueueFilterSide') is not None:
            self.message_queue_filter_side = m.get('MessageQueueFilterSide')

        if m.get('MessageQueueGrayEnable') is not None:
            self.message_queue_gray_enable = m.get('MessageQueueGrayEnable')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        if m.get('RecordCanaryDetail') is not None:
            self.record_canary_detail = m.get('RecordCanaryDetail')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

