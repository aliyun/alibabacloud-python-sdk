# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class ModifyDasOpsConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ModifyDasOpsConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The returned status code.
        self.code = code
        # SqlLogConfig
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # - **false**: The request failed.
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
            temp_model = main_models.ModifyDasOpsConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ModifyDasOpsConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_instance_id: str = None,
        eco_enable: bool = None,
        enable: bool = None,
        end_time: int = None,
        ops_enable: bool = None,
        order_id: int = None,
        start_time: int = None,
        status: str = None,
    ):
        # The payment method.
        self.charge_type = charge_type
        # The Alibaba Cloud Managed Services instance ID.
        self.commodity_instance_id = commodity_instance_id
        # Indicates whether DAS Economy Edition is enabled.
        self.eco_enable = eco_enable
        # Indicates whether the Alibaba Cloud Managed Services feature is enabled (including DAS Economy Edition).
        self.enable = enable
        # The end time. The value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time
        # Indicates whether Alibaba Cloud Managed Services is enabled.
        self.ops_enable = ops_enable
        # The order ID.
        self.order_id = order_id
        # The start time.
        self.start_time = start_time
        # The task status. Valid values:
        # - **INIT**: Pending scheduling.
        # - **RUNNING**: Running.
        # - **FAILED**: Failed.
        # - **CANCELED**: Canceled.
        # - **COMPLETED**: Completed.
        # 
        # > When the task is in the **COMPLETED** state, you can view the task result.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.commodity_instance_id is not None:
            result['CommodityInstanceId'] = self.commodity_instance_id

        if self.eco_enable is not None:
            result['EcoEnable'] = self.eco_enable

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ops_enable is not None:
            result['OpsEnable'] = self.ops_enable

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CommodityInstanceId') is not None:
            self.commodity_instance_id = m.get('CommodityInstanceId')

        if m.get('EcoEnable') is not None:
            self.eco_enable = m.get('EcoEnable')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OpsEnable') is not None:
            self.ops_enable = m.get('OpsEnable')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

