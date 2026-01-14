# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryTicketInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryTicketInfoResponseBodyResult = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the generated ticket.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryTicketInfoResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryTicketInfoResponseBodyResult(DaraModel):
    def __init__(
        self,
        access_ticket: str = None,
        cmpt_id: str = None,
        global_param: str = None,
        invalid_time: str = None,
        max_ticket_num: int = None,
        organization_id: str = None,
        register_time: str = None,
        used_ticket_num: int = None,
        user_id: str = None,
        watermark_param: str = None,
        works_id: str = None,
    ):
        # Notes.
        self.access_ticket = access_ticket
        # The ID of the component in the report.
        self.cmpt_id = cmpt_id
        # Global parameters.
        self.global_param = global_param
        # Expiration time of the note.
        self.invalid_time = invalid_time
        # The maximum number of supported bills.
        self.max_ticket_num = max_ticket_num
        # The ID of the organization.
        self.organization_id = organization_id
        # The registration time of the ticket.
        self.register_time = register_time
        # The number of bills that have been consumed.
        self.used_ticket_num = used_ticket_num
        # The user ID of the Quick BI.
        self.user_id = user_id
        # Set the watermarking parameters.
        self.watermark_param = watermark_param
        # The ID of the operations report.
        self.works_id = works_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_ticket is not None:
            result['AccessTicket'] = self.access_ticket

        if self.cmpt_id is not None:
            result['CmptId'] = self.cmpt_id

        if self.global_param is not None:
            result['GlobalParam'] = self.global_param

        if self.invalid_time is not None:
            result['InvalidTime'] = self.invalid_time

        if self.max_ticket_num is not None:
            result['MaxTicketNum'] = self.max_ticket_num

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        if self.register_time is not None:
            result['RegisterTime'] = self.register_time

        if self.used_ticket_num is not None:
            result['UsedTicketNum'] = self.used_ticket_num

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.watermark_param is not None:
            result['WatermarkParam'] = self.watermark_param

        if self.works_id is not None:
            result['WorksId'] = self.works_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTicket') is not None:
            self.access_ticket = m.get('AccessTicket')

        if m.get('CmptId') is not None:
            self.cmpt_id = m.get('CmptId')

        if m.get('GlobalParam') is not None:
            self.global_param = m.get('GlobalParam')

        if m.get('InvalidTime') is not None:
            self.invalid_time = m.get('InvalidTime')

        if m.get('MaxTicketNum') is not None:
            self.max_ticket_num = m.get('MaxTicketNum')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')

        if m.get('UsedTicketNum') is not None:
            self.used_ticket_num = m.get('UsedTicketNum')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WatermarkParam') is not None:
            self.watermark_param = m.get('WatermarkParam')

        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')

        return self

