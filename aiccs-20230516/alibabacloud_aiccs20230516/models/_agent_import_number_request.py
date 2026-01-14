# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aiccs20230516 import models as main_models
from darabonba.model import DaraModel

class AgentImportNumberRequest(DaraModel):
    def __init__(
        self,
        agent_id: int = None,
        agent_tag: str = None,
        call_type: int = None,
        customers: List[main_models.AgentImportNumberRequestCustomers] = None,
        gateway_id: int = None,
        out_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_id: int = None,
    ):
        # 坐席ID，可以为空，但agentId与agentTag必须其中1个有值。用于查询对应的坐席信息
        self.agent_id = agent_id
        # 坐席唯一标识（创建坐席时的用户唯一标识），可以为空，但agentId与agentTag必须其中1个有值。用于查询对应的坐席信息
        self.agent_tag = agent_tag
        # 外呼类型 可选项：1001：坐席-人工外呼，1002：坐席-AI外呼-不转人工，1003：坐席-AI外呼-接通转人工，1004：坐席-AI外呼-智能转人工"
        # 
        # This parameter is required.
        self.call_type = call_type
        # 具体用户信息，如手机号、姓名等，需根据具体任务参数要求传输。注：当callType为1001时，只会导入第1条数据
        # 
        # This parameter is required.
        self.customers = customers
        # 坐席-人工外呼选择的外呼线路，只针对callType=1001生效，其他callType不生效。如callType=1001，且gatewayId不传值，默认按系统的线路配置外呼
        self.gateway_id = gateway_id
        # 请求id，具有唯一性，用来做请求幂等处理，一个请求id有效期10分钟。不传则不做幂等处理
        self.out_id = out_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # AI话术ID 客户已制作并已发布/平台授权的AI话术ID，如callType=1001可不填；如callType=1002,1003或1004 ，必填。
        self.template_id = template_id

    def validate(self):
        if self.customers:
            for v1 in self.customers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_tag is not None:
            result['AgentTag'] = self.agent_tag

        if self.call_type is not None:
            result['CallType'] = self.call_type

        result['Customers'] = []
        if self.customers is not None:
            for k1 in self.customers:
                result['Customers'].append(k1.to_map() if k1 else None)

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentTag') is not None:
            self.agent_tag = m.get('AgentTag')

        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        self.customers = []
        if m.get('Customers') is not None:
            for k1 in m.get('Customers'):
                temp_model = main_models.AgentImportNumberRequestCustomers()
                self.customers.append(temp_model.from_map(k1))

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class AgentImportNumberRequestCustomers(DaraModel):
    def __init__(
        self,
        client_url: str = None,
        number: str = None,
        number_md5: str = None,
        properties: Dict[str, Any] = None,
        tag: str = None,
    ):
        # 客户详情URL,用于展示客户用户在客户业务系统的详细信息，做多80个字符
        self.client_url = client_url
        # 号码，如手机号等
        self.number = number
        # 用户电话号码MD5，和number两者必传一个
        self.number_md5 = number_md5
        # 用户具体信息。如AI话术模板没变量要求或为人工外呼，可为空(总长度500个字符，多余的会被剔除)
        self.properties = properties
        # 用户自定义标签,最多50个字符
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_url is not None:
            result['ClientUrl'] = self.client_url

        if self.number is not None:
            result['Number'] = self.number

        if self.number_md5 is not None:
            result['NumberMD5'] = self.number_md5

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientUrl') is not None:
            self.client_url = m.get('ClientUrl')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('NumberMD5') is not None:
            self.number_md5 = m.get('NumberMD5')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

