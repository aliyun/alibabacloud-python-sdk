# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class PutTargetsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.PutTargetsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. Valid values:
        # 
        # *   Success: The call succeeded.
        # *   Other codes: The call failed. For more information about error codes, see Error codes.
        self.code = code
        # The returned result.
        self.data = data
        # The error message that is returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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

        if m.get('Data') is not None:
            temp_model = main_models.PutTargetsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class PutTargetsResponseBodyData(DaraModel):
    def __init__(
        self,
        error_entries: List[main_models.PutTargetsResponseBodyDataErrorEntries] = None,
        error_entries_count: int = None,
    ):
        # The ID of the failed event target.
        self.error_entries = error_entries
        # The number of failed event targets. Valid values:
        # 
        # *   0: All event targets succeeded.
        # *   An integer other than 0: indicates the number of failed event targets.
        self.error_entries_count = error_entries_count

    def validate(self):
        if self.error_entries:
            for v1 in self.error_entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ErrorEntries'] = []
        if self.error_entries is not None:
            for k1 in self.error_entries:
                result['ErrorEntries'].append(k1.to_map() if k1 else None)

        if self.error_entries_count is not None:
            result['ErrorEntriesCount'] = self.error_entries_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_entries = []
        if m.get('ErrorEntries') is not None:
            for k1 in m.get('ErrorEntries'):
                temp_model = main_models.PutTargetsResponseBodyDataErrorEntries()
                self.error_entries.append(temp_model.from_map(k1))

        if m.get('ErrorEntriesCount') is not None:
            self.error_entries_count = m.get('ErrorEntriesCount')

        return self

class PutTargetsResponseBodyDataErrorEntries(DaraModel):
    def __init__(
        self,
        entry_id: str = None,
        error_code: str = None,
        error_message: str = None,
    ):
        # The ID of the failed event target.
        self.entry_id = entry_id
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entry_id is not None:
            result['EntryId'] = self.entry_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntryId') is not None:
            self.entry_id = m.get('EntryId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        return self

