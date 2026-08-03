# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class ListAICoachTaskSessionResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        session_list: List[main_models.ListAICoachTaskSessionResponseBodySessionList] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.session_list = session_list
        self.success = success

    def validate(self):
        if self.session_list:
            for v1 in self.session_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['sessionList'] = []
        if self.session_list is not None:
            for k1 in self.session_list:
                result['sessionList'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.session_list = []
        if m.get('sessionList') is not None:
            for k1 in m.get('sessionList'):
                temp_model = main_models.ListAICoachTaskSessionResponseBodySessionList()
                self.session_list.append(temp_model.from_map(k1))

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListAICoachTaskSessionResponseBodySessionList(DaraModel):
    def __init__(
        self,
        session_create_time: str = None,
        session_duration: int = None,
        session_id: str = None,
        session_status: int = None,
    ):
        self.session_create_time = session_create_time
        self.session_duration = session_duration
        self.session_id = session_id
        self.session_status = session_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_create_time is not None:
            result['sessionCreateTime'] = self.session_create_time

        if self.session_duration is not None:
            result['sessionDuration'] = self.session_duration

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.session_status is not None:
            result['sessionStatus'] = self.session_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionCreateTime') is not None:
            self.session_create_time = m.get('sessionCreateTime')

        if m.get('sessionDuration') is not None:
            self.session_duration = m.get('sessionDuration')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('sessionStatus') is not None:
            self.session_status = m.get('sessionStatus')

        return self

