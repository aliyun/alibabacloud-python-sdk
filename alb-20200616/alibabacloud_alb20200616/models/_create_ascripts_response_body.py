# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class CreateAScriptsResponseBody(DaraModel):
    def __init__(
        self,
        ascript_ids: List[main_models.CreateAScriptsResponseBodyAScriptIds] = None,
        job_id: str = None,
        request_id: str = None,
    ):
        # The AScript rule IDs.
        self.ascript_ids = ascript_ids
        # The asynchronous task ID.
        self.job_id = job_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.ascript_ids:
            for v1 in self.ascript_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AScriptIds'] = []
        if self.ascript_ids is not None:
            for k1 in self.ascript_ids:
                result['AScriptIds'].append(k1.to_map() if k1 else None)

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ascript_ids = []
        if m.get('AScriptIds') is not None:
            for k1 in m.get('AScriptIds'):
                temp_model = main_models.CreateAScriptsResponseBodyAScriptIds()
                self.ascript_ids.append(temp_model.from_map(k1))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateAScriptsResponseBodyAScriptIds(DaraModel):
    def __init__(
        self,
        ascript_id: str = None,
    ):
        # The AScript rule ID.
        self.ascript_id = ascript_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ascript_id is not None:
            result['AScriptId'] = self.ascript_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AScriptId') is not None:
            self.ascript_id = m.get('AScriptId')

        return self

