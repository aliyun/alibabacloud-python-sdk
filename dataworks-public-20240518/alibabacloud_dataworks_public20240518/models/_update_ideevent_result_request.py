# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateIDEEventResultRequest(DaraModel):
    def __init__(
        self,
        check_result: str = None,
        check_result_tip: str = None,
        extension_code: str = None,
        message_id: str = None,
    ):
        # The check status of the extension for this extension point event. Valid values:
        # 
        # - OK: The extension check for this extension point event passed.
        # - FAIL: The extension check for this extension point event failed. View and resolve the error promptly to avoid affecting the normal execution of subsequent programs.
        # - WARN: The extension check for this extension point event passed, but warnings exist.
        self.check_result = check_result
        # The summary of the check performed by the extension on this extension point event.
        # This information is displayed on your current development page. If the check has warnings or fails, you can use this summary to quickly identify the cause.
        self.check_result_tip = check_result_tip
        # The unique identifier of the extension.
        # You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and view the identifier on the Extensions tab of the Open Platform page.
        self.extension_code = extension_code
        # The message ID of the DataWorks open message. After an extension point event is triggered, you can obtain the message ID from the received event message.
        # 
        # 
        # <props="china">For more information about the message format, see [Message format](https://help.aliyun.com/document_detail/215367.html).
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_result is not None:
            result['CheckResult'] = self.check_result

        if self.check_result_tip is not None:
            result['CheckResultTip'] = self.check_result_tip

        if self.extension_code is not None:
            result['ExtensionCode'] = self.extension_code

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')

        if m.get('CheckResultTip') is not None:
            self.check_result_tip = m.get('CheckResultTip')

        if m.get('ExtensionCode') is not None:
            self.extension_code = m.get('ExtensionCode')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        return self

