# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWorkbenchEventResultRequest(DaraModel):
    def __init__(
        self,
        check_result: str = None,
        check_result_tip: str = None,
        extension_code: str = None,
        message_id: str = None,
    ):
        # The check result of the extension point event. Valid values: OK and Fail.
        # 
        # This parameter is required.
        self.check_result = check_result
        # The cause of the check failure.
        self.check_result_tip = check_result_tip
        # The code of the extension.
        # 
        # This parameter is required.
        self.extension_code = extension_code
        # The ID of the message received when the related extension point event is triggered after you enable message subscription by using the OpenEvent module.
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

