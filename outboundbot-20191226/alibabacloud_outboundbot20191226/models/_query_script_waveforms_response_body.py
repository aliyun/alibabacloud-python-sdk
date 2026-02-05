# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class QueryScriptWaveformsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        script_waveforms: List[main_models.QueryScriptWaveformsResponseBodyScriptWaveforms] = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.script_waveforms = script_waveforms
        self.success = success

    def validate(self):
        if self.script_waveforms:
            for v1 in self.script_waveforms:
                 if v1:
                    v1.validate()

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

        result['ScriptWaveforms'] = []
        if self.script_waveforms is not None:
            for k1 in self.script_waveforms:
                result['ScriptWaveforms'].append(k1.to_map() if k1 else None)

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

        self.script_waveforms = []
        if m.get('ScriptWaveforms') is not None:
            for k1 in m.get('ScriptWaveforms'):
                temp_model = main_models.QueryScriptWaveformsResponseBodyScriptWaveforms()
                self.script_waveforms.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryScriptWaveformsResponseBodyScriptWaveforms(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        file_name: str = None,
        script_content: str = None,
        script_id: str = None,
        script_waveform_id: str = None,
    ):
        self.file_id = file_id
        self.file_name = file_name
        self.script_content = script_content
        self.script_id = script_id
        self.script_waveform_id = script_waveform_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.script_content is not None:
            result['ScriptContent'] = self.script_content

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_waveform_id is not None:
            result['ScriptWaveformId'] = self.script_waveform_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('ScriptContent') is not None:
            self.script_content = m.get('ScriptContent')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptWaveformId') is not None:
            self.script_waveform_id = m.get('ScriptWaveformId')

        return self

