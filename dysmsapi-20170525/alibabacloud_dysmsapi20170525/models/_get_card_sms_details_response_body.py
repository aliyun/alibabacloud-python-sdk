# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class GetCardSmsDetailsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        card_send_detail_dto: main_models.GetCardSmsDetailsResponseBodyCardSendDetailDTO = None,
        code: str = None,
        message: str = None,
        success: bool = None,
    ):
        # The access denied details. This parameter is returned only when the RAM check fails.
        self.access_denied_detail = access_denied_detail
        # The card SMS sending result.
        self.card_send_detail_dto = card_send_detail_dto
        # The request status code.
        # * OK indicates that the request was successful.
        # * For other error codes, see [API error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The description of the status code.
        self.message = message
        # Indicates whether the call was successful. Valid values:
        # 
        # - **true**: The call was successful.
        # 
        # - **false**: The call failed.
        self.success = success

    def validate(self):
        if self.card_send_detail_dto:
            self.card_send_detail_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.card_send_detail_dto is not None:
            result['CardSendDetailDTO'] = self.card_send_detail_dto.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('CardSendDetailDTO') is not None:
            temp_model = main_models.GetCardSmsDetailsResponseBodyCardSendDetailDTO()
            self.card_send_detail_dto = temp_model.from_map(m.get('CardSendDetailDTO'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCardSmsDetailsResponseBodyCardSendDetailDTO(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        records: List[main_models.GetCardSmsDetailsResponseBodyCardSendDetailDTORecords] = None,
        total_count: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The list of card SMS sending records.
        self.records = records
        # The total count.
        self.total_count = total_count

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.GetCardSmsDetailsResponseBodyCardSendDetailDTORecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetCardSmsDetailsResponseBodyCardSendDetailDTORecords(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        out_id: str = None,
        phone_number: str = None,
        receive_date: str = None,
        receive_type: str = None,
        render_date: str = None,
        render_status: int = None,
        send_date: str = None,
        send_status: int = None,
        sms_content: str = None,
        template_code: str = None,
    ):
        # The sending error code.
        self.err_code = err_code
        # The outId passed by the customer.
        self.out_id = out_id
        # The phone number that received the SMS.
        self.phone_number = phone_number
        # The receive time.
        self.receive_date = receive_date
        # The SMS receive type.
        self.receive_type = receive_type
        # The render time.
        self.render_date = render_date
        # The parsing status. Valid values:
        # 
        # - 0: not parsed.
        # - 1: parsed successfully.
        # - 3: not parsed.
        self.render_status = render_status
        # The SMS sending time.
        self.send_date = send_date
        # The sending status. Valid values:
        # 
        # - 1: sending.
        # - 2: sending failed.
        # - 3: sending succeeded.
        # - 4: addressing failed.
        self.send_status = send_status
        # The SMS content. Only text SMS has a value.
        self.sms_content = sms_content
        # The template code.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.receive_date is not None:
            result['ReceiveDate'] = self.receive_date

        if self.receive_type is not None:
            result['ReceiveType'] = self.receive_type

        if self.render_date is not None:
            result['RenderDate'] = self.render_date

        if self.render_status is not None:
            result['RenderStatus'] = self.render_status

        if self.send_date is not None:
            result['SendDate'] = self.send_date

        if self.send_status is not None:
            result['SendStatus'] = self.send_status

        if self.sms_content is not None:
            result['SmsContent'] = self.sms_content

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('ReceiveDate') is not None:
            self.receive_date = m.get('ReceiveDate')

        if m.get('ReceiveType') is not None:
            self.receive_type = m.get('ReceiveType')

        if m.get('RenderDate') is not None:
            self.render_date = m.get('RenderDate')

        if m.get('RenderStatus') is not None:
            self.render_status = m.get('RenderStatus')

        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')

        if m.get('SendStatus') is not None:
            self.send_status = m.get('SendStatus')

        if m.get('SmsContent') is not None:
            self.sms_content = m.get('SmsContent')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

