# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetServiceRecordResponseBody(DaraModel):
    def __init__(
        self,
        record: main_models.GetServiceRecordResponseBodyRecord = None,
        request_id: str = None,
    ):
        # The record.
        self.record = record
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.record:
            self.record.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record is not None:
            result['record'] = self.record.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('record') is not None:
            temp_model = main_models.GetServiceRecordResponseBodyRecord()
            self.record = temp_model.from_map(m.get('record'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetServiceRecordResponseBodyRecord(DaraModel):
    def __init__(
        self,
        record_content: str = None,
        record_type: str = None,
        service_id: str = None,
        workspace: str = None,
    ):
        # The entry content in JSON string format. The returned content varies depending on the recordType.
        self.record_content = record_content
        # The type of the linked entry. Currently supported values:
        # logCorrelation: indicates application log association.
        self.record_type = record_type
        # The unique identifier of the service.
        self.service_id = service_id
        # The workspace.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_content is not None:
            result['recordContent'] = self.record_content

        if self.record_type is not None:
            result['recordType'] = self.record_type

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('recordContent') is not None:
            self.record_content = m.get('recordContent')

        if m.get('recordType') is not None:
            self.record_type = m.get('recordType')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

