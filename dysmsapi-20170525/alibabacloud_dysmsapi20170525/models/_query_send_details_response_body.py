# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QuerySendDetailsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        sms_send_detail_dtos: main_models.QuerySendDetailsResponseBodySmsSendDetailDTOs = None,
        total_count: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The details of the message.
        self.sms_send_detail_dtos = sms_send_detail_dtos
        # The number of sent messages.
        self.total_count = total_count

    def validate(self):
        if self.sms_send_detail_dtos:
            self.sms_send_detail_dtos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sms_send_detail_dtos is not None:
            result['SmsSendDetailDTOs'] = self.sms_send_detail_dtos.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SmsSendDetailDTOs') is not None:
            temp_model = main_models.QuerySendDetailsResponseBodySmsSendDetailDTOs()
            self.sms_send_detail_dtos = temp_model.from_map(m.get('SmsSendDetailDTOs'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QuerySendDetailsResponseBodySmsSendDetailDTOs(DaraModel):
    def __init__(
        self,
        sms_send_detail_dto: List[main_models.QuerySendDetailsResponseBodySmsSendDetailDTOsSmsSendDetailDTO] = None,
    ):
        self.sms_send_detail_dto = sms_send_detail_dto

    def validate(self):
        if self.sms_send_detail_dto:
            for v1 in self.sms_send_detail_dto:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SmsSendDetailDTO'] = []
        if self.sms_send_detail_dto is not None:
            for k1 in self.sms_send_detail_dto:
                result['SmsSendDetailDTO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sms_send_detail_dto = []
        if m.get('SmsSendDetailDTO') is not None:
            for k1 in m.get('SmsSendDetailDTO'):
                temp_model = main_models.QuerySendDetailsResponseBodySmsSendDetailDTOsSmsSendDetailDTO()
                self.sms_send_detail_dto.append(temp_model.from_map(k1))

        return self

class QuerySendDetailsResponseBodySmsSendDetailDTOsSmsSendDetailDTO(DaraModel):
    def __init__(
        self,
        content: str = None,
        err_code: str = None,
        out_id: str = None,
        phone_num: str = None,
        receive_date: str = None,
        send_date: str = None,
        send_status: int = None,
        template_code: str = None,
    ):
        # The content of the message.
        self.content = content
        # The status code returned by the carrier.
        # 
        # *   If the message is delivered, "DELIVERED" is returned.
        # *   For information about the error codes that may be returned if the message is not delivered, see [error codes](https://help.aliyun.com/document_detail/101347.html).
        self.err_code = err_code
        # The extended field.
        self.out_id = out_id
        # The mobile numbers of the recipients.
        self.phone_num = phone_num
        # The date and time when the message was received.
        self.receive_date = receive_date
        # The date and time when the message was sent.
        self.send_date = send_date
        # The delivery status of the message. Valid values:
        # 
        # *   **1**: The message has not received a delivery receipt yet.
        # *   **2**: The message failed to be delivered.
        # *   **3**: The message was delivered.
        self.send_status = send_status
        # The ID of the message template.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num

        if self.receive_date is not None:
            result['ReceiveDate'] = self.receive_date

        if self.send_date is not None:
            result['SendDate'] = self.send_date

        if self.send_status is not None:
            result['SendStatus'] = self.send_status

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')

        if m.get('ReceiveDate') is not None:
            self.receive_date = m.get('ReceiveDate')

        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')

        if m.get('SendStatus') is not None:
            self.send_status = m.get('SendStatus')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

