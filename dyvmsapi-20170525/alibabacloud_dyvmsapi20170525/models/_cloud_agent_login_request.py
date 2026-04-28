# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudAgentLoginRequest(DaraModel):
    def __init__(
        self,
        bind_tel: str = None,
        bind_type: int = None,
        cno: str = None,
        enterprise_id: int = None,
        login_status: int = None,
        pause_description: str = None,
    ):
        # 绑定电话
        # 
        # This parameter is required.
        self.bind_tel = bind_tel
        # 取值 1.普通电话,2.分机,3.webrtc </br>说明：绑定类型如果是分机则必须先让分机电话设备注册成功。如果绑定类型为webrtc，就算调用接口成功也是无法呼叫的。如果在企业设置页面开启了自适应绑定电话类型，则系统会根据绑定的号码来找到对应的绑定类型，使用系统找到的绑定类型，此处的设置优先级低。
        # 
        # This parameter is required.
        self.bind_type = bind_type
        # 座席工号；取值3-10位正整数
        # 
        # This parameter is required.
        self.cno = cno
        # 呼叫中心 id
        # 
        # This parameter is required.
        self.enterprise_id = enterprise_id
        # 登录状态，1：置闲，2：置忙，默认为1
        self.login_status = login_status
        # 置忙描述
        self.pause_description = pause_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_tel is not None:
            result['BindTel'] = self.bind_tel

        if self.bind_type is not None:
            result['BindType'] = self.bind_type

        if self.cno is not None:
            result['Cno'] = self.cno

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.login_status is not None:
            result['LoginStatus'] = self.login_status

        if self.pause_description is not None:
            result['PauseDescription'] = self.pause_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindTel') is not None:
            self.bind_tel = m.get('BindTel')

        if m.get('BindType') is not None:
            self.bind_type = m.get('BindType')

        if m.get('Cno') is not None:
            self.cno = m.get('Cno')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('LoginStatus') is not None:
            self.login_status = m.get('LoginStatus')

        if m.get('PauseDescription') is not None:
            self.pause_description = m.get('PauseDescription')

        return self

