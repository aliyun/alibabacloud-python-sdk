# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20230516 import models as main_models
from darabonba.model import DaraModel

class QueryAgentInfoResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        message: str = None,
        model: main_models.QueryAgentInfoResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
        timestamp: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success
        self.timestamp = timestamp

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            temp_model = main_models.QueryAgentInfoResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class QueryAgentInfoResponseBodyModel(DaraModel):
    def __init__(
        self,
        account: str = None,
        active: int = None,
        agent_extension: int = None,
        agent_group_ids: List[int] = None,
        agent_group_list: List[main_models.QueryAgentInfoResponseBodyModelAgentGroupList] = None,
        agent_id: int = None,
        agent_status: int = None,
        agent_tag: str = None,
        create_time: str = None,
        extension_pwd: str = None,
        extension_server: str = None,
        name: str = None,
        ws_protocol: str = None,
        ws_register_address: str = None,
    ):
        # 坐席账号
        self.account = account
        # 账号启用状态，0-停用，1-启用，默认1
        self.active = active
        # 坐席分机号
        self.agent_extension = agent_extension
        # 坐席组ID列表
        self.agent_group_ids = agent_group_ids
        # 坐席组列表
        self.agent_group_list = agent_group_list
        # 坐席ID
        self.agent_id = agent_id
        # 坐席状态，1:在线；2:忙碌；3:小休；4:离线
        self.agent_status = agent_status
        # 坐席标签
        self.agent_tag = agent_tag
        # 创建时间
        self.create_time = create_time
        # 分机密码
        self.extension_pwd = extension_pwd
        # 分机注册地址
        self.extension_server = extension_server
        # 坐席名称
        self.name = name
        # WebSocket分机注册协议
        self.ws_protocol = ws_protocol
        # WebSocket分机注册地址
        self.ws_register_address = ws_register_address

    def validate(self):
        if self.agent_group_list:
            for v1 in self.agent_group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.active is not None:
            result['Active'] = self.active

        if self.agent_extension is not None:
            result['AgentExtension'] = self.agent_extension

        if self.agent_group_ids is not None:
            result['AgentGroupIds'] = self.agent_group_ids

        result['AgentGroupList'] = []
        if self.agent_group_list is not None:
            for k1 in self.agent_group_list:
                result['AgentGroupList'].append(k1.to_map() if k1 else None)

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status

        if self.agent_tag is not None:
            result['AgentTag'] = self.agent_tag

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.extension_pwd is not None:
            result['ExtensionPwd'] = self.extension_pwd

        if self.extension_server is not None:
            result['ExtensionServer'] = self.extension_server

        if self.name is not None:
            result['Name'] = self.name

        if self.ws_protocol is not None:
            result['WsProtocol'] = self.ws_protocol

        if self.ws_register_address is not None:
            result['WsRegisterAddress'] = self.ws_register_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('AgentExtension') is not None:
            self.agent_extension = m.get('AgentExtension')

        if m.get('AgentGroupIds') is not None:
            self.agent_group_ids = m.get('AgentGroupIds')

        self.agent_group_list = []
        if m.get('AgentGroupList') is not None:
            for k1 in m.get('AgentGroupList'):
                temp_model = main_models.QueryAgentInfoResponseBodyModelAgentGroupList()
                self.agent_group_list.append(temp_model.from_map(k1))

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')

        if m.get('AgentTag') is not None:
            self.agent_tag = m.get('AgentTag')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExtensionPwd') is not None:
            self.extension_pwd = m.get('ExtensionPwd')

        if m.get('ExtensionServer') is not None:
            self.extension_server = m.get('ExtensionServer')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('WsProtocol') is not None:
            self.ws_protocol = m.get('WsProtocol')

        if m.get('WsRegisterAddress') is not None:
            self.ws_register_address = m.get('WsRegisterAddress')

        return self

class QueryAgentInfoResponseBodyModelAgentGroupList(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        group_name: str = None,
    ):
        # 坐席组ID
        self.group_id = group_id
        # 坐席组名称
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

