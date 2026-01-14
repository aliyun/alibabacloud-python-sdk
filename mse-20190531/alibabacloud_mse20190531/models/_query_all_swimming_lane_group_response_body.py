# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class QueryAllSwimmingLaneGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.QueryAllSwimmingLaneGroupResponseBodyData] = None,
        dynamic_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. A value of 200 is returned if the request is successful.
        self.code = code
        # The details of the data.
        self.data = data
        # The dynamic part in the error message.
        self.dynamic_message = dynamic_message
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The returned message.
        # 
        # *   If the request is successful, a success message is returned.
        # *   If the request fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

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

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryAllSwimmingLaneGroupResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAllSwimmingLaneGroupResponseBodyData(DaraModel):
    def __init__(
        self,
        app_ids: str = None,
        canary_model: int = None,
        entry_app: str = None,
        id: int = None,
        message_queue_filter_side: str = None,
        message_queue_gray_enable: bool = None,
        name: str = None,
        namespace: str = None,
        paths: str = None,
        record_canary_detail: bool = None,
        region: str = None,
        swim_version: int = None,
        user_id: str = None,
    ):
        self.app_ids = app_ids
        self.canary_model = canary_model
        self.entry_app = entry_app
        self.id = id
        self.message_queue_filter_side = message_queue_filter_side
        self.message_queue_gray_enable = message_queue_gray_enable
        self.name = name
        self.namespace = namespace
        self.paths = paths
        self.record_canary_detail = record_canary_detail
        self.region = region
        self.swim_version = swim_version
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

        if self.swim_version is not None:
            result['SwimVersion'] = self.swim_version

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')

        if m.get('CanaryModel') is not None:
            self.canary_model = m.get('CanaryModel')

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

        if m.get('SwimVersion') is not None:
            self.swim_version = m.get('SwimVersion')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

