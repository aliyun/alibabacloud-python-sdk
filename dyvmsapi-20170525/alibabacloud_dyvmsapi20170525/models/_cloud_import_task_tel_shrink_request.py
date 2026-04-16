# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudImportTaskTelShrinkRequest(DaraModel):
    def __init__(
        self,
        bridge_voice_path: str = None,
        bridge_voice_type: int = None,
        enterprise_id: int = None,
        file_id: int = None,
        import_tel_auto_start: int = None,
        is_repeat: int = None,
        name: str = None,
        owner_id: int = None,
        priority: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: int = None,
        task_tel_list_shrink: str = None,
    ):
        # 座席接听时自动在双侧播放开场白语音，指定语音变量值；企业语音库里的语音变量值
        self.bridge_voice_path = bridge_voice_path
        # 座席接听时自动在双侧播放开场白语音类型；1. 公共语音库；2. 企业语音库，静态话术； 3. 企业语音库，动态话术（座席号），传bridgeVoicePath后生效，默认为3
        self.bridge_voice_type = bridge_voice_type
        # 呼叫中心 id
        # 
        # This parameter is required.
        self.enterprise_id = enterprise_id
        # 批次Id；传此值表示在批次中增加号码
        self.file_id = file_id
        # 是否自动启动任务；0:不自动启动 1:自动启动，默认为0
        self.import_tel_auto_start = import_tel_auto_start
        # 是否排重；0.不排重 1.任务内排重 2.导入号码排重 3.批次内排重，默认为1。注：任务内排重与批次内排重不能同时支持，如果中途切换，则从本次切换开始进行排重。
        self.is_repeat = is_repeat
        # 批次名称
        # 
        # This parameter is required.
        self.name = name
        self.owner_id = owner_id
        # 优先级；默认0，值越大越优先，最大999999
        self.priority = priority
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 任务Id
        # 
        # This parameter is required.
        self.task_id = task_id
        # 任务号码列表；CtiLinkTaskTel中只有Tel是必选字段，长度大小不超过8MB 注：获取导入失败明细，需配置[事件推送](../字段定义/推送变量和值/预测外呼导入号码失败推送变量.md)
        # 
        # This parameter is required.
        self.task_tel_list_shrink = task_tel_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bridge_voice_path is not None:
            result['BridgeVoicePath'] = self.bridge_voice_path

        if self.bridge_voice_type is not None:
            result['BridgeVoiceType'] = self.bridge_voice_type

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.import_tel_auto_start is not None:
            result['ImportTelAutoStart'] = self.import_tel_auto_start

        if self.is_repeat is not None:
            result['IsRepeat'] = self.is_repeat

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_tel_list_shrink is not None:
            result['TaskTelList'] = self.task_tel_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BridgeVoicePath') is not None:
            self.bridge_voice_path = m.get('BridgeVoicePath')

        if m.get('BridgeVoiceType') is not None:
            self.bridge_voice_type = m.get('BridgeVoiceType')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('ImportTelAutoStart') is not None:
            self.import_tel_auto_start = m.get('ImportTelAutoStart')

        if m.get('IsRepeat') is not None:
            self.is_repeat = m.get('IsRepeat')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskTelList') is not None:
            self.task_tel_list_shrink = m.get('TaskTelList')

        return self

