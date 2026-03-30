# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class ListScriptsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListScriptsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
        self.request_id = request_id

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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListScriptsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListScriptsResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        scripts: List[main_models.ListScriptsResponseBodyDataScripts] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.scripts = scripts
        self.total_count = total_count

    def validate(self):
        if self.scripts:
            for v1 in self.scripts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Scripts'] = []
        if self.scripts is not None:
            for k1 in self.scripts:
                result['Scripts'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.scripts = []
        if m.get('Scripts') is not None:
            for k1 in m.get('Scripts'):
                temp_model = main_models.ListScriptsResponseBodyDataScripts()
                self.scripts.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListScriptsResponseBodyDataScripts(DaraModel):
    def __init__(
        self,
        concurrency: int = None,
        created_time: int = None,
        description: str = None,
        draft_version_id: str = None,
        name: str = None,
        nlu_access_type: str = None,
        nlu_engine: str = None,
        number: str = None,
        published_version_id: str = None,
        script_id: str = None,
        status: str = None,
        updated_time: int = None,
    ):
        self.concurrency = concurrency
        self.created_time = created_time
        self.description = description
        self.draft_version_id = draft_version_id
        self.name = name
        self.nlu_access_type = nlu_access_type
        self.nlu_engine = nlu_engine
        self.number = number
        self.published_version_id = published_version_id
        self.script_id = script_id
        self.status = status
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.draft_version_id is not None:
            result['DraftVersionId'] = self.draft_version_id

        if self.name is not None:
            result['Name'] = self.name

        if self.nlu_access_type is not None:
            result['NluAccessType'] = self.nlu_access_type

        if self.nlu_engine is not None:
            result['NluEngine'] = self.nlu_engine

        if self.number is not None:
            result['Number'] = self.number

        if self.published_version_id is not None:
            result['PublishedVersionId'] = self.published_version_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.status is not None:
            result['Status'] = self.status

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DraftVersionId') is not None:
            self.draft_version_id = m.get('DraftVersionId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NluAccessType') is not None:
            self.nlu_access_type = m.get('NluAccessType')

        if m.get('NluEngine') is not None:
            self.nlu_engine = m.get('NluEngine')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('PublishedVersionId') is not None:
            self.published_version_id = m.get('PublishedVersionId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

