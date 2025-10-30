# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSampleDataResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        error_message: str = None,
        has_sample_data: bool = None,
        request_id: str = None,
        sample_data_status: str = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The error message returned if an error occurs. This message does not affect the execution of the operation.
        self.error_message = error_message
        # Indicates whether a sample dataset is loaded to the instance. Valid values:
        # 
        # *   **true**: A sample dataset is loaded.
        # *   **false**: No sample dataset is loaded.
        self.has_sample_data = has_sample_data
        # The ID of the request.
        self.request_id = request_id
        # The loading status of the sample dataset. Valid values:
        # 
        # *   **loaded**
        # *   **loading**
        # *   **unload**
        self.sample_data_status = sample_data_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.has_sample_data is not None:
            result['HasSampleData'] = self.has_sample_data

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sample_data_status is not None:
            result['SampleDataStatus'] = self.sample_data_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HasSampleData') is not None:
            self.has_sample_data = m.get('HasSampleData')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SampleDataStatus') is not None:
            self.sample_data_status = m.get('SampleDataStatus')

        return self

