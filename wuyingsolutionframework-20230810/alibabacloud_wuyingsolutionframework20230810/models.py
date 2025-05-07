# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class SendOpsMessageToTerminalRequest(TeaModel):
    def __init__(
        self,
        message_body: str = None,
        office_region_id: str = None,
        ops_action: str = None,
        serial_no: str = None,
        wait_for_ack: bool = None,
        wait_for_msg: bool = None,
    ):
        self.message_body = message_body
        self.office_region_id = office_region_id
        self.ops_action = ops_action
        self.serial_no = serial_no
        self.wait_for_ack = wait_for_ack
        self.wait_for_msg = wait_for_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_body is not None:
            result['MessageBody'] = self.message_body
        if self.office_region_id is not None:
            result['OfficeRegionId'] = self.office_region_id
        if self.ops_action is not None:
            result['OpsAction'] = self.ops_action
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.wait_for_ack is not None:
            result['WaitForAck'] = self.wait_for_ack
        if self.wait_for_msg is not None:
            result['WaitForMsg'] = self.wait_for_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageBody') is not None:
            self.message_body = m.get('MessageBody')
        if m.get('OfficeRegionId') is not None:
            self.office_region_id = m.get('OfficeRegionId')
        if m.get('OpsAction') is not None:
            self.ops_action = m.get('OpsAction')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('WaitForAck') is not None:
            self.wait_for_ack = m.get('WaitForAck')
        if m.get('WaitForMsg') is not None:
            self.wait_for_msg = m.get('WaitForMsg')
        return self


class SendOpsMessageToTerminalResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendOpsMessageToTerminalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendOpsMessageToTerminalResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendOpsMessageToTerminalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


