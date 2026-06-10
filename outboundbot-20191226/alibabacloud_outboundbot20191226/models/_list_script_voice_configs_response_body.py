# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListScriptVoiceConfigsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        script_voice_configs: main_models.ListScriptVoiceConfigsResponseBodyScriptVoiceConfigs = None,
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
        # The paginated list of script voice configurations.
        self.script_voice_configs = script_voice_configs
        # Indicates whether the request succeeded.
        self.success = success

    def validate(self):
        if self.script_voice_configs:
            self.script_voice_configs.validate()

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

        if self.script_voice_configs is not None:
            result['ScriptVoiceConfigs'] = self.script_voice_configs.to_map()

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

        if m.get('ScriptVoiceConfigs') is not None:
            temp_model = main_models.ListScriptVoiceConfigsResponseBodyScriptVoiceConfigs()
            self.script_voice_configs = temp_model.from_map(m.get('ScriptVoiceConfigs'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListScriptVoiceConfigsResponseBodyScriptVoiceConfigs(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListScriptVoiceConfigsResponseBodyScriptVoiceConfigsList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # An array of script voice configuration objects.
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
                temp_model = main_models.ListScriptVoiceConfigsResponseBodyScriptVoiceConfigsList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListScriptVoiceConfigsResponseBodyScriptVoiceConfigsList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        script_content: str = None,
        script_id: str = None,
        script_voice_config_id: str = None,
        script_waveform_relation: str = None,
        source: str = None,
        type: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The text content of the script.
        self.script_content = script_content
        # The script ID.
        self.script_id = script_id
        # The ID of the voice configuration.
        self.script_voice_config_id = script_voice_config_id
        # The relationship between the script and the audio file.
        self.script_waveform_relation = script_waveform_relation
        # The source of the script.
        self.source = source
        # The voice type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.script_content is not None:
            result['ScriptContent'] = self.script_content

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_voice_config_id is not None:
            result['ScriptVoiceConfigId'] = self.script_voice_config_id

        if self.script_waveform_relation is not None:
            result['ScriptWaveformRelation'] = self.script_waveform_relation

        if self.source is not None:
            result['Source'] = self.source

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScriptContent') is not None:
            self.script_content = m.get('ScriptContent')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptVoiceConfigId') is not None:
            self.script_voice_config_id = m.get('ScriptVoiceConfigId')

        if m.get('ScriptWaveformRelation') is not None:
            self.script_waveform_relation = m.get('ScriptWaveformRelation')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

