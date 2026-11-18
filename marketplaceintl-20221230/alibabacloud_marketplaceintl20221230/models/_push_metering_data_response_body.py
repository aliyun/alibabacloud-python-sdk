# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushMeteringDataResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        dynamic_message: str = None,
        force_fatal: bool = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_message = dynamic_message
        self.force_fatal = force_fatal
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.force_fatal is not None:
            result['ForceFatal'] = self.force_fatal

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ForceFatal') is not None:
            self.force_fatal = m.get('ForceFatal')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

