# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListVoiceCloneResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListVoiceCloneResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The API status code.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The message returned by the API.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
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

        if m.get('Data') is not None:
            temp_model = main_models.ListVoiceCloneResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListVoiceCloneResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        voice_clones: List[main_models.ListVoiceCloneResponseBodyDataVoiceClones] = None,
    ):
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of cloned voices that meet the filter conditions.
        self.total_count = total_count
        # The list of cloned voices.
        self.voice_clones = voice_clones

    def validate(self):
        if self.voice_clones:
            for v1 in self.voice_clones:
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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VoiceClones'] = []
        if self.voice_clones is not None:
            for k1 in self.voice_clones:
                result['VoiceClones'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.voice_clones = []
        if m.get('VoiceClones') is not None:
            for k1 in m.get('VoiceClones'):
                temp_model = main_models.ListVoiceCloneResponseBodyDataVoiceClones()
                self.voice_clones.append(temp_model.from_map(k1))

        return self

class ListVoiceCloneResponseBodyDataVoiceClones(DaraModel):
    def __init__(
        self,
        creator: str = None,
        engine: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        instance_id: str = None,
        model: str = None,
        status: str = None,
        voice_id: str = None,
        voice_name: str = None,
    ):
        # The Alibaba Cloud account ID of the creator of the voice.
        self.creator = creator
        # The type of the text-to-speech (TTS) engine used by the voice.
        self.engine = engine
        # The creation time. The value is a UNIX timestamp in milliseconds.
        self.gmt_create = gmt_create
        # The last modification time. The value is a UNIX timestamp in milliseconds.
        self.gmt_modified = gmt_modified
        # The instance ID.
        self.instance_id = instance_id
        # The identifier of the model used for cloning.
        self.model = model
        # The voice status. Valid values: Enabled (available) and Disabled (unavailable).
        self.status = status
        # The voice ID.
        self.voice_id = voice_id
        # The voice name.
        self.voice_name = voice_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.model is not None:
            result['Model'] = self.model

        if self.status is not None:
            result['Status'] = self.status

        if self.voice_id is not None:
            result['VoiceId'] = self.voice_id

        if self.voice_name is not None:
            result['VoiceName'] = self.voice_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VoiceId') is not None:
            self.voice_id = m.get('VoiceId')

        if m.get('VoiceName') is not None:
            self.voice_name = m.get('VoiceName')

        return self

