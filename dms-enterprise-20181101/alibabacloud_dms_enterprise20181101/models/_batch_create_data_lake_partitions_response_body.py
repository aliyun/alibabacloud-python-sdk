# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class BatchCreateDataLakePartitionsResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        partitions: List[main_models.DLPartition] = None,
        request_id: str = None,
        success: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message that is returned if the request failed.
        self.error_message = error_message
        # The details about the new partitions. This parameter is returned when the NeedResult parameter is set to true.
        self.partitions = partitions
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request succeeded.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.partitions:
            for v1 in self.partitions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        result['Partitions'] = []
        if self.partitions is not None:
            for k1 in self.partitions:
                result['Partitions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        self.partitions = []
        if m.get('Partitions') is not None:
            for k1 in m.get('Partitions'):
                temp_model = main_models.DLPartition()
                self.partitions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

