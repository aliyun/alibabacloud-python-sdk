# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CallbackExtensionRequest(DaraModel):
    def __init__(
        self,
        check_message: str = None,
        check_result: str = None,
        extension_code: str = None,
        message_id: str = None,
    ):
        # The check message of the extension point event. If CheckResult is set to FAIL, you must provide the failure cause.
        self.check_message = check_message
        # The check status of the extension point event. Valid values:
        # 
        # *   OK: The event passes the check.
        # *   FAIL: The event fails to pass the check. You must check and handle the reported error at the earliest opportunity to ensure that your program is run as expected.
        # *   WARN: The event passes the check, but an alert is reported.
        # 
        # This parameter is required.
        self.check_result = check_result
        # The unique code of the extension.
        # 
        # This parameter is required.
        self.extension_code = extension_code
        # The message ID in DataWorks OpenEvent. You can obtain the ID from a received message when an extension point event is triggered.
        # 
        # This parameter is required.
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_message is not None:
            result['CheckMessage'] = self.check_message

        if self.check_result is not None:
            result['CheckResult'] = self.check_result

        if self.extension_code is not None:
            result['ExtensionCode'] = self.extension_code

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckMessage') is not None:
            self.check_message = m.get('CheckMessage')

        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')

        if m.get('ExtensionCode') is not None:
            self.extension_code = m.get('ExtensionCode')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        return self

