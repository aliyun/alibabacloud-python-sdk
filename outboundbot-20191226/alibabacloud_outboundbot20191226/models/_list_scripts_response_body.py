# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListScriptsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        scripts: main_models.ListScriptsResponseBodyScripts = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.scripts = scripts
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
            temp_model = main_models.ListScriptsResponseBodyScripts()
            self.scripts = temp_model.from_map(m.get('Scripts'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListScriptsResponseBodyScripts(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListScriptsResponseBodyScriptsList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
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
                temp_model = main_models.ListScriptsResponseBodyScriptsList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListScriptsResponseBodyScriptsList(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        agent_llm: bool = None,
        create_time: int = None,
        debug_status: str = None,
        emotion_enable: bool = None,
        industry: str = None,
        is_debug_drafted: bool = None,
        is_drafted: bool = None,
        is_preset: bool = None,
        long_wait_enable: bool = None,
        mini_playback_enable: bool = None,
        new_barge_in_enable: bool = None,
        nlu_access_type: str = None,
        nlu_engine: str = None,
        nlu_profile: main_models.ListScriptsResponseBodyScriptsListNluProfile = None,
        reject_reason: str = None,
        scene: str = None,
        script_description: str = None,
        script_id: str = None,
        script_name: str = None,
        status: str = None,
        update_time: int = None,
        agent_id: int = None,
    ):
        self.agent_key = agent_key
        self.agent_llm = agent_llm
        self.create_time = create_time
        self.debug_status = debug_status
        self.emotion_enable = emotion_enable
        self.industry = industry
        self.is_debug_drafted = is_debug_drafted
        self.is_drafted = is_drafted
        self.is_preset = is_preset
        self.long_wait_enable = long_wait_enable
        self.mini_playback_enable = mini_playback_enable
        self.new_barge_in_enable = new_barge_in_enable
        self.nlu_access_type = nlu_access_type
        self.nlu_engine = nlu_engine
        self.nlu_profile = nlu_profile
        self.reject_reason = reject_reason
        self.scene = scene
        self.script_description = script_description
        self.script_id = script_id
        self.script_name = script_name
        self.status = status
        self.update_time = update_time
        self.agent_id = agent_id

    def validate(self):
        if self.nlu_profile:
            self.nlu_profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.agent_llm is not None:
            result['AgentLlm'] = self.agent_llm

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.debug_status is not None:
            result['DebugStatus'] = self.debug_status

        if self.emotion_enable is not None:
            result['EmotionEnable'] = self.emotion_enable

        if self.industry is not None:
            result['Industry'] = self.industry

        if self.is_debug_drafted is not None:
            result['IsDebugDrafted'] = self.is_debug_drafted

        if self.is_drafted is not None:
            result['IsDrafted'] = self.is_drafted

        if self.is_preset is not None:
            result['IsPreset'] = self.is_preset

        if self.long_wait_enable is not None:
            result['LongWaitEnable'] = self.long_wait_enable

        if self.mini_playback_enable is not None:
            result['MiniPlaybackEnable'] = self.mini_playback_enable

        if self.new_barge_in_enable is not None:
            result['NewBargeInEnable'] = self.new_barge_in_enable

        if self.nlu_access_type is not None:
            result['NluAccessType'] = self.nlu_access_type

        if self.nlu_engine is not None:
            result['NluEngine'] = self.nlu_engine

        if self.nlu_profile is not None:
            result['NluProfile'] = self.nlu_profile.to_map()

        if self.reject_reason is not None:
            result['RejectReason'] = self.reject_reason

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

        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('AgentLlm') is not None:
            self.agent_llm = m.get('AgentLlm')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DebugStatus') is not None:
            self.debug_status = m.get('DebugStatus')

        if m.get('EmotionEnable') is not None:
            self.emotion_enable = m.get('EmotionEnable')

        if m.get('Industry') is not None:
            self.industry = m.get('Industry')

        if m.get('IsDebugDrafted') is not None:
            self.is_debug_drafted = m.get('IsDebugDrafted')

        if m.get('IsDrafted') is not None:
            self.is_drafted = m.get('IsDrafted')

        if m.get('IsPreset') is not None:
            self.is_preset = m.get('IsPreset')

        if m.get('LongWaitEnable') is not None:
            self.long_wait_enable = m.get('LongWaitEnable')

        if m.get('MiniPlaybackEnable') is not None:
            self.mini_playback_enable = m.get('MiniPlaybackEnable')

        if m.get('NewBargeInEnable') is not None:
            self.new_barge_in_enable = m.get('NewBargeInEnable')

        if m.get('NluAccessType') is not None:
            self.nlu_access_type = m.get('NluAccessType')

        if m.get('NluEngine') is not None:
            self.nlu_engine = m.get('NluEngine')

        if m.get('NluProfile') is not None:
            temp_model = main_models.ListScriptsResponseBodyScriptsListNluProfile()
            self.nlu_profile = temp_model.from_map(m.get('NluProfile'))

        if m.get('RejectReason') is not None:
            self.reject_reason = m.get('RejectReason')

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

        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        return self

class ListScriptsResponseBodyScriptsListNluProfile(DaraModel):
    def __init__(
        self,
        fc_function: str = None,
        fc_http_trigger_url: str = None,
        fc_region: str = None,
    ):
        self.fc_function = fc_function
        self.fc_http_trigger_url = fc_http_trigger_url
        self.fc_region = fc_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fc_function is not None:
            result['FcFunction'] = self.fc_function

        if self.fc_http_trigger_url is not None:
            result['FcHttpTriggerUrl'] = self.fc_http_trigger_url

        if self.fc_region is not None:
            result['FcRegion'] = self.fc_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FcFunction') is not None:
            self.fc_function = m.get('FcFunction')

        if m.get('FcHttpTriggerUrl') is not None:
            self.fc_http_trigger_url = m.get('FcHttpTriggerUrl')

        if m.get('FcRegion') is not None:
            self.fc_region = m.get('FcRegion')

        return self

