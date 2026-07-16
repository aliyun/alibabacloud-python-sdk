# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ListDataAgentAccuracyTestInstancesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDataAgentAccuracyTestInstancesResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        success: str = None,
        timestamp: str = None,
        total: str = None,
    ):
        # The response struct.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The maximum number of entries returned per page. You can use this parameter together with NextToken to implement paging.
        self.max_results = max_results
        # The pagination token.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The operation timestamp.
        self.timestamp = timestamp
        # The total number of records.
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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListDataAgentAccuracyTestInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListDataAgentAccuracyTestInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        accuracy_test_ins_id: str = None,
        agent_id: str = None,
        creator: str = None,
        file_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        language: str = None,
        max_concurrent: str = None,
        mode: int = None,
        name: str = None,
        need_delete: str = None,
        workspace_id: str = None,
    ):
        # The accuracy test instance ID.
        self.accuracy_test_ins_id = accuracy_test_ins_id
        # The custom agent ID.
        self.agent_id = agent_id
        # The UID of the workspace creator.
        self.creator = creator
        # The test set file ID.
        self.file_id = file_id
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The language used for the analysis task.
        self.language = language
        # The maximum number of concurrent sessions during testing.
        self.max_concurrent = max_concurrent
        # The analysis mode to be tested.
        self.mode = mode
        # The custom agent name.
        self.name = name
        # Specifies whether sessions are displayed after analysis. This feature is not currently supported.
        self.need_delete = need_delete
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accuracy_test_ins_id is not None:
            result['AccuracyTestInsId'] = self.accuracy_test_ins_id

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.language is not None:
            result['Language'] = self.language

        if self.max_concurrent is not None:
            result['MaxConcurrent'] = self.max_concurrent

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        if self.need_delete is not None:
            result['NeedDelete'] = self.need_delete

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccuracyTestInsId') is not None:
            self.accuracy_test_ins_id = m.get('AccuracyTestInsId')

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('MaxConcurrent') is not None:
            self.max_concurrent = m.get('MaxConcurrent')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NeedDelete') is not None:
            self.need_delete = m.get('NeedDelete')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

