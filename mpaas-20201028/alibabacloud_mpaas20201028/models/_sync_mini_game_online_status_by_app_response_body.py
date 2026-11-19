# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class SyncMiniGameOnlineStatusByAppResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        content: main_models.SyncMiniGameOnlineStatusByAppResponseBodyContent = None,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.content = content
        self.error_code = error_code
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Content') is not None:
            temp_model = main_models.SyncMiniGameOnlineStatusByAppResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SyncMiniGameOnlineStatusByAppResponseBodyContent(DaraModel):
    def __init__(
        self,
        current_online_status: int = None,
        mini_program_code: str = None,
        status_changed: bool = None,
    ):
        self.current_online_status = current_online_status
        self.mini_program_code = mini_program_code
        self.status_changed = status_changed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_online_status is not None:
            result['CurrentOnlineStatus'] = self.current_online_status

        if self.mini_program_code is not None:
            result['MiniProgramCode'] = self.mini_program_code

        if self.status_changed is not None:
            result['StatusChanged'] = self.status_changed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentOnlineStatus') is not None:
            self.current_online_status = m.get('CurrentOnlineStatus')

        if m.get('MiniProgramCode') is not None:
            self.mini_program_code = m.get('MiniProgramCode')

        if m.get('StatusChanged') is not None:
            self.status_changed = m.get('StatusChanged')

        return self

