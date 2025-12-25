# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceConnectivityResponseBody(DaraModel):
    def __init__(
        self,
        conn_check_error_code: str = None,
        conn_check_error_message: str = None,
        conn_check_result: str = None,
        db_instance_name: str = None,
        request_id: str = None,
    ):
        # The error code for connection diagnosis. Valid values:
        # 
        # *   **SRC_IP_NOT_IN_USER_WHITELIST**: The source IP address is not added to the whitelist.
        # *   **CONNECTION_ABNORMAL**: The connection to the cluster is normal.
        self.conn_check_error_code = conn_check_error_code
        # The error message for connection diagnosis.
        self.conn_check_error_message = conn_check_error_message
        # The connection diagnosis result. Valid values:
        # 
        # *   **Success**
        # *   **Failed**
        self.conn_check_result = conn_check_result
        # The instance ID.
        self.db_instance_name = db_instance_name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conn_check_error_code is not None:
            result['ConnCheckErrorCode'] = self.conn_check_error_code

        if self.conn_check_error_message is not None:
            result['ConnCheckErrorMessage'] = self.conn_check_error_message

        if self.conn_check_result is not None:
            result['ConnCheckResult'] = self.conn_check_result

        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnCheckErrorCode') is not None:
            self.conn_check_error_code = m.get('ConnCheckErrorCode')

        if m.get('ConnCheckErrorMessage') is not None:
            self.conn_check_error_message = m.get('ConnCheckErrorMessage')

        if m.get('ConnCheckResult') is not None:
            self.conn_check_result = m.get('ConnCheckResult')

        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

