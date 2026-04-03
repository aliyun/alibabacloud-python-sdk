# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class IMBotInfo(DaraModel):
    def __init__(
        self,
        agent_runtime_id: str = None,
        bot_biz_id: str = None,
        bot_biz_type: str = None,
        bot_mode: str = None,
        bot_name: str = None,
        created_at: str = None,
        current_instances: int = None,
        description: str = None,
        id: str = None,
        im_channel_server_resource_name: str = None,
        last_message_time: str = None,
        metadata: main_models.IMBotMetadata = None,
        status: str = None,
        tenant_id: str = None,
        updated_at: str = None,
    ):
        self.agent_runtime_id = agent_runtime_id
        self.bot_biz_id = bot_biz_id
        # dingtalk、wecom、feishu、custom
        self.bot_biz_type = bot_biz_type
        # standard、custom
        self.bot_mode = bot_mode
        self.bot_name = bot_name
        self.created_at = created_at
        # 可选；来自账号元数据 scaling.currentInstances，同一租户下各 Bot 响应中值相同
        self.current_instances = current_instances
        # Bot 描述信息
        self.description = description
        self.id = id
        self.im_channel_server_resource_name = im_channel_server_resource_name
        # 可选
        self.last_message_time = last_message_time
        self.metadata = metadata
        self.status = status
        self.tenant_id = tenant_id
        self.updated_at = updated_at

    def validate(self):
        if self.metadata:
            self.metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_runtime_id is not None:
            result['agentRuntimeId'] = self.agent_runtime_id

        if self.bot_biz_id is not None:
            result['botBizId'] = self.bot_biz_id

        if self.bot_biz_type is not None:
            result['botBizType'] = self.bot_biz_type

        if self.bot_mode is not None:
            result['botMode'] = self.bot_mode

        if self.bot_name is not None:
            result['botName'] = self.bot_name

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.current_instances is not None:
            result['currentInstances'] = self.current_instances

        if self.description is not None:
            result['description'] = self.description

        if self.id is not None:
            result['id'] = self.id

        if self.im_channel_server_resource_name is not None:
            result['imChannelServerResourceName'] = self.im_channel_server_resource_name

        if self.last_message_time is not None:
            result['lastMessageTime'] = self.last_message_time

        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentRuntimeId') is not None:
            self.agent_runtime_id = m.get('agentRuntimeId')

        if m.get('botBizId') is not None:
            self.bot_biz_id = m.get('botBizId')

        if m.get('botBizType') is not None:
            self.bot_biz_type = m.get('botBizType')

        if m.get('botMode') is not None:
            self.bot_mode = m.get('botMode')

        if m.get('botName') is not None:
            self.bot_name = m.get('botName')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('currentInstances') is not None:
            self.current_instances = m.get('currentInstances')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('imChannelServerResourceName') is not None:
            self.im_channel_server_resource_name = m.get('imChannelServerResourceName')

        if m.get('lastMessageTime') is not None:
            self.last_message_time = m.get('lastMessageTime')

        if m.get('metadata') is not None:
            temp_model = main_models.IMBotMetadata()
            self.metadata = temp_model.from_map(m.get('metadata'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

