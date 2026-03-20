# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx220190430 import models as main_models
from darabonba.model import DaraModel

class ListJobScriptHistoryResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListJobScriptHistoryResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The information about the jobs.
        self.data = data
        # The additional information returned only if an error occurs.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # true
        # 
        # false
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
            temp_model = main_models.ListJobScriptHistoryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListJobScriptHistoryResponseBodyData(DaraModel):
    def __init__(
        self,
        job_script_history_infos: List[main_models.ListJobScriptHistoryResponseBodyDataJobScriptHistoryInfos] = None,
    ):
        # The information about the job\\"s historical scripts.
        self.job_script_history_infos = job_script_history_infos

    def validate(self):
        if self.job_script_history_infos:
            for v1 in self.job_script_history_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JobScriptHistoryInfos'] = []
        if self.job_script_history_infos is not None:
            for k1 in self.job_script_history_infos:
                result['JobScriptHistoryInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_script_history_infos = []
        if m.get('JobScriptHistoryInfos') is not None:
            for k1 in m.get('JobScriptHistoryInfos'):
                temp_model = main_models.ListJobScriptHistoryResponseBodyDataJobScriptHistoryInfos()
                self.job_script_history_infos.append(temp_model.from_map(k1))

        return self

class ListJobScriptHistoryResponseBodyDataJobScriptHistoryInfos(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        creator: str = None,
        script_content: str = None,
        versiones_description: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The creator.
        self.creator = creator
        # The script content.
        self.script_content = script_content
        # The description of the script version.
        self.versiones_description = versiones_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.script_content is not None:
            result['ScriptContent'] = self.script_content

        if self.versiones_description is not None:
            result['VersionesDescription'] = self.versiones_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('ScriptContent') is not None:
            self.script_content = m.get('ScriptContent')

        if m.get('VersionesDescription') is not None:
            self.versiones_description = m.get('VersionesDescription')

        return self

