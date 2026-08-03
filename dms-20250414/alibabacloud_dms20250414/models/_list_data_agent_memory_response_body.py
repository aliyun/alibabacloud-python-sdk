# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ListDataAgentMemoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListDataAgentMemoryResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        timestamp: str = None,
    ):
        # The status code. A value of Success indicates success.
        self.code = code
        # The response struct.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message returned if the call failed.
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.                                 
        # - **false**: The request failed.
        self.success = success
        # The operation timestamp.
        self.timestamp = timestamp

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListDataAgentMemoryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class ListDataAgentMemoryResponseBodyData(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDataAgentMemoryResponseBodyDataData] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The response struct.
        self.data = data
        # The current page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
        self.total = total

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListDataAgentMemoryResponseBodyDataData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListDataAgentMemoryResponseBodyDataData(DaraModel):
    def __init__(
        self,
        content: str = None,
        from_id: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        hint_level: int = None,
        mem_from: str = None,
        status: str = None,
        uuid: str = None,
    ):
        # The memory content.
        self.content = content
        # The memory source ID.
        self.from_id = from_id
        # The creation time.
        self.gmt_created = gmt_created
        # The modification time.
        self.gmt_modified = gmt_modified
        # The memory hit level (hotness).
        self.hint_level = hint_level
        # The memory source.
        self.mem_from = mem_from
        # The memory status.
        self.status = status
        # The memory UUID.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.from_id is not None:
            result['FromId'] = self.from_id

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.hint_level is not None:
            result['HintLevel'] = self.hint_level

        if self.mem_from is not None:
            result['MemFrom'] = self.mem_from

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FromId') is not None:
            self.from_id = m.get('FromId')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('HintLevel') is not None:
            self.hint_level = m.get('HintLevel')

        if m.get('MemFrom') is not None:
            self.mem_from = m.get('MemFrom')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

