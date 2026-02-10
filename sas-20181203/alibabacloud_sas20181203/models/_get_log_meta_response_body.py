# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetLogMetaResponseBody(DaraModel):
    def __init__(
        self,
        log_meta: main_models.GetLogMetaResponseBodyLogMeta = None,
        request_id: str = None,
    ):
        # The data of a data shipping task.
        self.log_meta = log_meta
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.log_meta:
            self.log_meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_meta is not None:
            result['LogMeta'] = self.log_meta.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogMeta') is not None:
            temp_model = main_models.GetLogMetaResponseBodyLogMeta()
            self.log_meta = temp_model.from_map(m.get('LogMeta'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetLogMetaResponseBodyLogMeta(DaraModel):
    def __init__(
        self,
        log_store: str = None,
        project: str = None,
        status: str = None,
    ):
        # The name of the dedicated Logstore in which logs are stored.
        self.log_store = log_store
        # The Simple Log Service project.
        self.project = project
        # The status of a data shipping task of a log. Valid values:
        # 
        # *   **enabled**
        # *   **disabled**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_store is not None:
            result['LogStore'] = self.log_store

        if self.project is not None:
            result['Project'] = self.project

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

