# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class ExecDataCheckToggleRequest(DaraModel):
    def __init__(
        self,
        params: List[main_models.ExecDataCheckToggleRequestParams] = None,
    ):
        # The task scheduling parameter list. Each item must contain id, lastBatchId, and isScheduled.
        # 
        # This parameter is required.
        self.params = params

    def validate(self):
        if self.params:
            for v1 in self.params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['params'] = []
        if self.params is not None:
            for k1 in self.params:
                result['params'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.params = []
        if m.get('params') is not None:
            for k1 in m.get('params'):
                temp_model = main_models.ExecDataCheckToggleRequestParams()
                self.params.append(temp_model.from_map(k1))

        return self

class ExecDataCheckToggleRequestParams(DaraModel):
    def __init__(
        self,
        id: int = None,
        is_scheduled: int = None,
        last_batch_id: int = None,
    ):
        # The task ID.
        # 
        # This parameter is required.
        self.id = id
        # Specifies whether to enable scheduling. Valid values:
        # 
        # - 0: Disabled.
        # - 1: Enabled.
        # 
        # This parameter is required.
        self.is_scheduled = is_scheduled
        # The most recent batch number.
        # 
        # This parameter is required.
        self.last_batch_id = last_batch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.is_scheduled is not None:
            result['isScheduled'] = self.is_scheduled

        if self.last_batch_id is not None:
            result['lastBatchId'] = self.last_batch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isScheduled') is not None:
            self.is_scheduled = m.get('isScheduled')

        if m.get('lastBatchId') is not None:
            self.last_batch_id = m.get('lastBatchId')

        return self

