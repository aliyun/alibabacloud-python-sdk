# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetPluginsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.GetPluginsResponseBodyData] = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned code.
        self.code = code
        # The data entries returned.
        self.data = data
        # The dynamic part in the error message.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetPluginsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetPluginsResponseBodyData(DaraModel):
    def __init__(
        self,
        category: int = None,
        config_check: str = None,
        id: int = None,
        max_version: str = None,
        mode: int = None,
        name: str = None,
        new_version_publishing_flag: bool = None,
        phase: int = None,
        primary_user: str = None,
        priority: int = None,
        publish_state: int = None,
        status: str = None,
        summary: str = None,
        summary_en: str = None,
        version: str = None,
        wasm_file: str = None,
        wasm_lang: int = None,
    ):
        # The type of the plug-in. Valid values:
        # 
        # 0: custom
        # 
        # 1: permission authorization
        # 
        # 2: security protection
        # 
        # 3: transmission protocol
        # 
        # 4: traffic control
        # 
        # 5: traffic observation
        self.category = category
        # The information about the plug-in configuration used for checking.
        self.config_check = config_check
        # The ID of the plug-in.
        self.id = id
        self.max_version = max_version
        self.mode = mode
        # The name of the plug-in.
        self.name = name
        self.new_version_publishing_flag = new_version_publishing_flag
        # The execution stage of the plug-in.
        # 
        # *   0: default stage
        # *   1: authorization stage
        # *   2: authentication stage
        # *   3: statistics stage
        self.phase = phase
        # The ID of the creator.
        self.primary_user = primary_user
        # The execution priority of the plug-in. A larger value indicates a higher priority.
        self.priority = priority
        # The publish status.
        self.publish_state = publish_state
        # Indicates whether the plug-in is enabled.
        # 
        # *   0: disabled
        # *   1: enabled
        self.status = status
        # The summary of the plug-in.
        self.summary = summary
        self.summary_en = summary_en
        # The version of the plug-in.
        self.version = version
        # The URL of the Object Storage Service (OSS) bucket that stores the WebAssembly plug-in.
        self.wasm_file = wasm_file
        # The WebAssembly language. Valid values:
        # 
        # *   0: C++
        # *   1: TinyGo
        # *   2: Rust
        # *   3: AssemblyScript
        # *   4: Zig
        self.wasm_lang = wasm_lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.config_check is not None:
            result['ConfigCheck'] = self.config_check

        if self.id is not None:
            result['Id'] = self.id

        if self.max_version is not None:
            result['MaxVersion'] = self.max_version

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        if self.new_version_publishing_flag is not None:
            result['NewVersionPublishingFlag'] = self.new_version_publishing_flag

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.primary_user is not None:
            result['PrimaryUser'] = self.primary_user

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.publish_state is not None:
            result['PublishState'] = self.publish_state

        if self.status is not None:
            result['Status'] = self.status

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.summary_en is not None:
            result['SummaryEn'] = self.summary_en

        if self.version is not None:
            result['Version'] = self.version

        if self.wasm_file is not None:
            result['WasmFile'] = self.wasm_file

        if self.wasm_lang is not None:
            result['WasmLang'] = self.wasm_lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ConfigCheck') is not None:
            self.config_check = m.get('ConfigCheck')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MaxVersion') is not None:
            self.max_version = m.get('MaxVersion')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NewVersionPublishingFlag') is not None:
            self.new_version_publishing_flag = m.get('NewVersionPublishingFlag')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('PrimaryUser') is not None:
            self.primary_user = m.get('PrimaryUser')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('PublishState') is not None:
            self.publish_state = m.get('PublishState')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('SummaryEn') is not None:
            self.summary_en = m.get('SummaryEn')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('WasmFile') is not None:
            self.wasm_file = m.get('WasmFile')

        if m.get('WasmLang') is not None:
            self.wasm_lang = m.get('WasmLang')

        return self

