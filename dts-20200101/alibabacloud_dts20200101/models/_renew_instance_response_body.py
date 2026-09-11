# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewInstanceResponseBody(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        code: str = None,
        dts_job_id: str = None,
        dynamic_message: str = None,
        end_time: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The billing method. Set the value to **PREPAY**, which indicates the subscription billing method.
        self.charge_type = charge_type
        # The error code.
        # 
        # > This parameter will be deprecated.
        self.code = code
        # The ID of the data synchronization or change tracking task.
        self.dts_job_id = dts_job_id
        # The dynamic error message, which is used to replace the %**s** variable in the **ErrMessage** response parameter.
        # 
        # > If **ErrMessage** returns **The Value of Input Parameter %s is not valid** and **DynamicMessage** returns **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The time when the renewal instance expires. The time is displayed in the format of <i>yyyy-MM-dd</i>T<i>HH:mm:ssZZZ</i> (UTC).
        # 
        # > **ZZZ** indicates the full time zone offset ("+" or "-" followed by hours and minutes), for example, **+00:00**.
        self.end_time = end_time
        # The error code returned when the call fails.
        self.err_code = err_code
        # The error message returned when the call fails.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The instance ID.
        self.instance_id = instance_id
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.code is not None:
            result['Code'] = self.code

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

