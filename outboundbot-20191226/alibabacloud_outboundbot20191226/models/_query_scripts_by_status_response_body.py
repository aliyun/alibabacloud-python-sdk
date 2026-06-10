# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class QueryScriptsByStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        scripts: main_models.QueryScriptsByStatusResponseBodyScripts = None,
        success: bool = None,
    ):
        # The API status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The scenarios.
        self.scripts = scripts
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.scripts:
            self.scripts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scripts is not None:
            result['Scripts'] = self.scripts.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Scripts') is not None:
            temp_model = main_models.QueryScriptsByStatusResponseBodyScripts()
            self.scripts = temp_model.from_map(m.get('Scripts'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryScriptsByStatusResponseBodyScripts(DaraModel):
    def __init__(
        self,
        list: List[main_models.QueryScriptsByStatusResponseBodyScriptsList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of scenarios.
        self.list = list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.QueryScriptsByStatusResponseBodyScriptsList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryScriptsByStatusResponseBodyScriptsList(DaraModel):
    def __init__(
        self,
        applied_version: str = None,
        debug_status: str = None,
        debug_version: str = None,
        industry: str = None,
        is_debug_drafted: bool = None,
        is_drafted: bool = None,
        scene: str = None,
        script_description: str = None,
        script_id: str = None,
        script_name: str = None,
        status: str = None,
        update_time: int = None,
    ):
        # The version ID.
        self.applied_version = applied_version
        # The debug status.
        self.debug_status = debug_status
        # The debug version.
        self.debug_version = debug_version
        # The industry.
        self.industry = industry
        # Indicates whether the debug version is a draft.
        self.is_debug_drafted = is_debug_drafted
        # Indicates whether the version is a draft.
        self.is_drafted = is_drafted
        # The scenario.
        self.scene = scene
        # The script description.
        self.script_description = script_description
        # The scenario ID.
        self.script_id = script_id
        # The scenario name.
        self.script_name = script_name
        # The status of the application version. Valid values:
        # 
        # - **DRAFTED**: The script is a draft.
        # 
        # - **INITIALIZE_IN_PROGRESS**: The script is being initialized.
        # 
        # - **PUBLISHED**: The script is published.
        # 
        # - **PUBLISH_IN_PROGRESS**: The script is being published.
        # 
        # - **ROLLBACK_IN_PROGRESS**: The script is being rolled back.
        # 
        # - **EXAMINE_IN_PROGRESS**: The script is pending approval.
        # 
        # - **PUBLISHED_AND_EXAMINE_IN_PROGRESS**: The script is published and pending approval.
        # 
        # - **PUBLISH_FAILED**: The script failed to be published.
        # 
        # - **ROLLBACK_FAILED**: The script failed to be rolled back.
        # 
        # - **IMPORT_IN_PROGRESS**: The script is being imported.
        # 
        # - **IMPORT_FAILED**: The script failed to be imported.
        self.status = status
        # The time when the script was last updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applied_version is not None:
            result['AppliedVersion'] = self.applied_version

        if self.debug_status is not None:
            result['DebugStatus'] = self.debug_status

        if self.debug_version is not None:
            result['DebugVersion'] = self.debug_version

        if self.industry is not None:
            result['Industry'] = self.industry

        if self.is_debug_drafted is not None:
            result['IsDebugDrafted'] = self.is_debug_drafted

        if self.is_drafted is not None:
            result['IsDrafted'] = self.is_drafted

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.script_description is not None:
            result['ScriptDescription'] = self.script_description

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_name is not None:
            result['ScriptName'] = self.script_name

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppliedVersion') is not None:
            self.applied_version = m.get('AppliedVersion')

        if m.get('DebugStatus') is not None:
            self.debug_status = m.get('DebugStatus')

        if m.get('DebugVersion') is not None:
            self.debug_version = m.get('DebugVersion')

        if m.get('Industry') is not None:
            self.industry = m.get('Industry')

        if m.get('IsDebugDrafted') is not None:
            self.is_debug_drafted = m.get('IsDebugDrafted')

        if m.get('IsDrafted') is not None:
            self.is_drafted = m.get('IsDrafted')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('ScriptDescription') is not None:
            self.script_description = m.get('ScriptDescription')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

