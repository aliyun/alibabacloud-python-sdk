# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetDBInstanceConnectivityDiagnosisResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDBInstanceConnectivityDiagnosisResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The returned status code.
        self.code = code
        # The details.
        self.data = data
        # The returned message.
        # >If the request is successful, **Successful** is returned. If the request fails, an error message is returned, such as an error code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # * **true**: The request is successful.
        # * **false**: The request fails.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetDBInstanceConnectivityDiagnosisResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDBInstanceConnectivityDiagnosisResponseBodyData(DaraModel):
    def __init__(
        self,
        conn_check_error_code: str = None,
        conn_check_error_message: str = None,
        fail_type: str = None,
        instance_id: str = None,
        success: bool = None,
    ):
        # The outlier detection item. Valid values:
        # 
        # - **SRC_IP_NOT_IN_USER_WHITELIST**: The source IP address is not added to the user whitelist.
        # - **VIP_NOT_EXISTS**: The ALB instance corresponding to the VIP does not exist.
        # - **RS_NOT_EXISTS**: The RS is not properly mounted.
        # - **VIP_TUNNEL_ID_NOT_CONSISTENT**: The TUNNEL ID used by the VPC-type VIP is inconsistent with the actual TUNNEL ID of the VPC.
        # - **VIP_VPC_CLOUD_INSTANCE_NOT_EXISTS**: The VPC-type VIP does not exist.
        # - **VIP_IS_NOT_NGLB**: The NGLB pattern is shutdown for the VIP.
        # - **CUSTINS_NOT_ASSOCIATE_ECS_SECURITY_GROUP**: The instance is not associated with a security group.
        # - **SRC_IP_NOT_IN_USER_WHITELIST**: The source IP address is not added to the user whitelist.
        # - **SRC_IP_NOT_IN_ADMIN_WHITELIST**: The source IP address is not added to the management machine whitelist.
        # - **SRC_IP_NOT_IN_ECS_SECURITY_GROUP**: The source IP address is not added to the security group associated with the instance.
        # - **VPC_INSTANCE_IP_NOT_WORKING_STATUS**: The VPC IP address is in an abnormal state.
        self.conn_check_error_code = conn_check_error_code
        # The details of the outlier detection item.
        self.conn_check_error_message = conn_check_error_message
        # The exception type. Valid values:
        # 
        # - **0**: The issue can be resolved by the user.
        # - **1**: The issue requires on-duty personnel to resolve.
        self.fail_type = fail_type
        # The instance ID.
        self.instance_id = instance_id
        # Indicates whether the check is passed. Valid values:
        # 
        # - **true**: The check is passed.
        # - **false**: The check is not passed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conn_check_error_code is not None:
            result['connCheckErrorCode'] = self.conn_check_error_code

        if self.conn_check_error_message is not None:
            result['connCheckErrorMessage'] = self.conn_check_error_message

        if self.fail_type is not None:
            result['failType'] = self.fail_type

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('connCheckErrorCode') is not None:
            self.conn_check_error_code = m.get('connCheckErrorCode')

        if m.get('connCheckErrorMessage') is not None:
            self.conn_check_error_message = m.get('connCheckErrorMessage')

        if m.get('failType') is not None:
            self.fail_type = m.get('failType')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

