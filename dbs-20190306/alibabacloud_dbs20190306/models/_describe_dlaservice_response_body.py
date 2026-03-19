# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDLAServiceResponseBody(DaraModel):
    def __init__(
        self,
        auto_add: bool = None,
        err_code: str = None,
        err_message: str = None,
        have_job_failed: bool = None,
        http_status_code: int = None,
        request_id: str = None,
        state: str = None,
        success: bool = None,
    ):
        # Specifies whether to enable the feature of automatically adding incremental data to a data lake. If this feature is enabled, DBS adds the backup sets that are newly generated to the data lake that is created for the backup schedule. Valid values:
        # 
        # - **true**: enables the feature.
        # 
        # - **false**: disables the feature.
        self.auto_add = auto_add
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # Indicates whether a failed DLA task exists in the return result. Valid values:
        # 
        # - **true**: A failed DLA task exists.
        # 
        # - **false**: No failed DLA task exists.
        self.have_job_failed = have_job_failed
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # The status of the DLA service for the backup schedule. Valid values:
        # 
        # - **Running**: DLA is running.
        # 
        # - **Closing**: DLA is being disabled.
        # 
        # - **Closed**: DLA is disabled.
        self.state = state
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_add is not None:
            result['AutoAdd'] = self.auto_add

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.have_job_failed is not None:
            result['HaveJobFailed'] = self.have_job_failed

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.state is not None:
            result['State'] = self.state

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoAdd') is not None:
            self.auto_add = m.get('AutoAdd')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HaveJobFailed') is not None:
            self.have_job_failed = m.get('HaveJobFailed')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

