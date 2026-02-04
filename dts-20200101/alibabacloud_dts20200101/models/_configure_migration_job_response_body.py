# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigureMigrationJobResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future.
        self.err_code = err_code
        # The ID of the request.
        self.err_message = err_message
        # The start offset of incremental data migration. The value is a UNIX timestamp. Unit: seconds.
        self.request_id = request_id
        # The SID of the Oracle database.
        # 
        # >  You must specify this parameter only if the **DestinationEndpoint.EngineName** parameter is set to **Oracle** and the **Oracle** database is deployed in a non-RAC architecture.
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

