# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListAIAgentVoiceprintsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        voiceprints: List[main_models.ListAIAgentVoiceprintsResponseBodyVoiceprints] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The total number of voiceprints that match the query criteria.
        self.total_count = total_count
        # The voiceprints.
        self.voiceprints = voiceprints

    def validate(self):
        if self.voiceprints:
            for v1 in self.voiceprints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Voiceprints'] = []
        if self.voiceprints is not None:
            for k1 in self.voiceprints:
                result['Voiceprints'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.voiceprints = []
        if m.get('Voiceprints') is not None:
            for k1 in m.get('Voiceprints'):
                temp_model = main_models.ListAIAgentVoiceprintsResponseBodyVoiceprints()
                self.voiceprints.append(temp_model.from_map(k1))

        return self

class ListAIAgentVoiceprintsResponseBodyVoiceprints(DaraModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        voiceprint_id: str = None,
    ):
        # The creation time of the voiceprint.
        self.gmt_create = gmt_create
        # The last modification time of the voiceprint.
        self.gmt_modified = gmt_modified
        # The unique identifier for the voiceprint.
        self.voiceprint_id = voiceprint_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.voiceprint_id is not None:
            result['VoiceprintId'] = self.voiceprint_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('VoiceprintId') is not None:
            self.voiceprint_id = m.get('VoiceprintId')

        return self

