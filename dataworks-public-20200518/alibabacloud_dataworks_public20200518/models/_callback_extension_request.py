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
        # The reason for the failure when CheckResult is set to FAIL.
        self.check_message = check_message
        # The check status of the extension program for the extension point event. Valid values:
        # - OK: The extension program check for the extension point event passed.
        # - FAIL: The extension program check for the extension point event failed. View and resolve the error promptly to avoid affecting the normal execution of subsequent programs.
        # - WARN: The extension program check for the extension point event passed, but warnings exist.
        # 
        # This parameter is required.
        self.check_result = check_result
        # The unique code of the extension program.
        # 
        # This parameter is required.
        self.extension_code = extension_code
        # The message ID of the DataWorks open message. After an extension point event is triggered, you can obtain the message ID from the received event message.
        # 
        # <props="china">For more information about the message format, see [Message format](https://help.aliyun.com/document_detail/215367.html).
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

