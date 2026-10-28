# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PreCheckCreateGadOrderResponseBody(DaraModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        instance_id: str = None,
        region_id: str = None,
        request_id: str = None,
        success: str = None,
        task_id: str = None,
    ):
        # The dynamic error code. This parameter is deprecated and will be phased out.
        self.dynamic_code = dynamic_code
        # The dynamic error message, which is used to replace %s in the error message returned by the ErrMessage parameter.
        # 
        # > If the ErrMessage parameter returns The Value of Input Parameter %s is not valid and the DynamicMessage parameter returns JobId, the JobId request parameter is invalid.
        self.dynamic_message = dynamic_message
        # The error code returned if the call fails.
        self.err_code = err_code
        # The error message returned if the call fails.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the global active instance group.
        self.instance_id = instance_id
        # The ID of the region where the instance resides. For more information, see the list of supported regions.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed.
        self.success = success
        # The ID of the precheck task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

