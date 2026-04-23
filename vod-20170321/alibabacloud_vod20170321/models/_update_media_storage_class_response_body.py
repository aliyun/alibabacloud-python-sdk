# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class UpdateMediaStorageClassResponseBody(DaraModel):
    def __init__(
        self,
        forbidden_list: main_models.UpdateMediaStorageClassResponseBodyForbiddenList = None,
        ignored_list: main_models.UpdateMediaStorageClassResponseBodyIgnoredList = None,
        request_id: str = None,
        status: str = None,
    ):
        self.forbidden_list = forbidden_list
        self.ignored_list = ignored_list
        # The ID of the request.
        self.request_id = request_id
        # The state of the task. Valid values:
        # 
        # *   **Processing**
        # *   **Failed**
        self.status = status

    def validate(self):
        if self.forbidden_list:
            self.forbidden_list.validate()
        if self.ignored_list:
            self.ignored_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forbidden_list is not None:
            result['ForbiddenList'] = self.forbidden_list.to_map()

        if self.ignored_list is not None:
            result['IgnoredList'] = self.ignored_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForbiddenList') is not None:
            temp_model = main_models.UpdateMediaStorageClassResponseBodyForbiddenList()
            self.forbidden_list = temp_model.from_map(m.get('ForbiddenList'))

        if m.get('IgnoredList') is not None:
            temp_model = main_models.UpdateMediaStorageClassResponseBodyIgnoredList()
            self.ignored_list = temp_model.from_map(m.get('IgnoredList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class UpdateMediaStorageClassResponseBodyIgnoredList(DaraModel):
    def __init__(
        self,
        media_id: List[str] = None,
    ):
        self.media_id = media_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

class UpdateMediaStorageClassResponseBodyForbiddenList(DaraModel):
    def __init__(
        self,
        media_forbidden_reason_dto: List[main_models.UpdateMediaStorageClassResponseBodyForbiddenListMediaForbiddenReasonDTO] = None,
    ):
        self.media_forbidden_reason_dto = media_forbidden_reason_dto

    def validate(self):
        if self.media_forbidden_reason_dto:
            for v1 in self.media_forbidden_reason_dto:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MediaForbiddenReasonDTO'] = []
        if self.media_forbidden_reason_dto is not None:
            for k1 in self.media_forbidden_reason_dto:
                result['MediaForbiddenReasonDTO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.media_forbidden_reason_dto = []
        if m.get('MediaForbiddenReasonDTO') is not None:
            for k1 in m.get('MediaForbiddenReasonDTO'):
                temp_model = main_models.UpdateMediaStorageClassResponseBodyForbiddenListMediaForbiddenReasonDTO()
                self.media_forbidden_reason_dto.append(temp_model.from_map(k1))

        return self

class UpdateMediaStorageClassResponseBodyForbiddenListMediaForbiddenReasonDTO(DaraModel):
    def __init__(
        self,
        media_id: str = None,
        reason: str = None,
    ):
        self.media_id = media_id
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

