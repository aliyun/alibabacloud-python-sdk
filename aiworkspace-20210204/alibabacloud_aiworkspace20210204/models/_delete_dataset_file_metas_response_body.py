# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class DeleteDatasetFileMetasResponseBody(DaraModel):
    def __init__(
        self,
        failed_details: List[main_models.DatasetFileMetaResponse] = None,
        request_id: str = None,
        status: bool = None,
    ):
        # The metadata records that fail to be deleted for the dataset files.
        self.failed_details = failed_details
        # The request ID.
        self.request_id = request_id
        # Indicates whether the metadata records of all dataset files were deleted. The value true indicates that the metadata records of all dataset files are deleted. If the value is false, view the failure details specified by FailedDetails.
        self.status = status

    def validate(self):
        if self.failed_details:
            for v1 in self.failed_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailedDetails'] = []
        if self.failed_details is not None:
            for k1 in self.failed_details:
                result['FailedDetails'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_details = []
        if m.get('FailedDetails') is not None:
            for k1 in m.get('FailedDetails'):
                temp_model = main_models.DatasetFileMetaResponse()
                self.failed_details.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

