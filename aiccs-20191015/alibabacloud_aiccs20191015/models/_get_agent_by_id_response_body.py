# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class GetAgentByIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAgentByIdResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.GetAgentByIdResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAgentByIdResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: int = None,
        create_user_name: str = None,
        foreign_key: str = None,
        foreign_nick: str = None,
        real_name: str = None,
        servicer_type: int = None,
        show_name: str = None,
    ):
        self.agent_id = agent_id
        self.create_user_name = create_user_name
        self.foreign_key = foreign_key
        self.foreign_nick = foreign_nick
        self.real_name = real_name
        self.servicer_type = servicer_type
        self.show_name = show_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.foreign_key is not None:
            result['ForeignKey'] = self.foreign_key

        if self.foreign_nick is not None:
            result['ForeignNick'] = self.foreign_nick

        if self.real_name is not None:
            result['RealName'] = self.real_name

        if self.servicer_type is not None:
            result['ServicerType'] = self.servicer_type

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('ForeignKey') is not None:
            self.foreign_key = m.get('ForeignKey')

        if m.get('ForeignNick') is not None:
            self.foreign_nick = m.get('ForeignNick')

        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')

        if m.get('ServicerType') is not None:
            self.servicer_type = m.get('ServicerType')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        return self

