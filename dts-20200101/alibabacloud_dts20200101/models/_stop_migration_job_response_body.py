# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopMigrationJobResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The ID of the data migration instance. You can call the **DescribeMigrationJobs** operation to query all data migration instances.
        self.err_code = err_code
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future.
        self.err_message = err_message
        # The ID of the region where the data migration instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.request_id = request_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The **ClientToken** parameter can contain only ASCII characters and cannot exceed 64 characters in length.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

