# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListRepoBuildRecordLogResponseBody(DaraModel):
    def __init__(
        self,
        build_record_logs: List[main_models.ListRepoBuildRecordLogResponseBodyBuildRecordLogs] = None,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The log content of the image building record.
        self.build_record_logs = build_record_logs
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The page number of the returned page.
        self.page_no = page_no
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.build_record_logs:
            for v1 in self.build_record_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BuildRecordLogs'] = []
        if self.build_record_logs is not None:
            for k1 in self.build_record_logs:
                result['BuildRecordLogs'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.build_record_logs = []
        if m.get('BuildRecordLogs') is not None:
            for k1 in m.get('BuildRecordLogs'):
                temp_model = main_models.ListRepoBuildRecordLogResponseBodyBuildRecordLogs()
                self.build_record_logs.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRepoBuildRecordLogResponseBodyBuildRecordLogs(DaraModel):
    def __init__(
        self,
        build_stage: str = None,
        line_number: int = None,
        message: str = None,
    ):
        # The stage of the building that is recorded in the log entry.
        self.build_stage = build_stage
        # The line number of the log entry.
        self.line_number = line_number
        # The content of the log.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_stage is not None:
            result['BuildStage'] = self.build_stage

        if self.line_number is not None:
            result['LineNumber'] = self.line_number

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildStage') is not None:
            self.build_stage = m.get('BuildStage')

        if m.get('LineNumber') is not None:
            self.line_number = m.get('LineNumber')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

