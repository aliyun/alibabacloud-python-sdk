# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CreateIMBotInput(DaraModel):
    def __init__(
        self,
        bot_biz_id: str = None,
        bot_biz_secret: str = None,
        bot_biz_type: str = None,
        bot_mode: str = None,
        bot_name: str = None,
        description: str = None,
        metadata: main_models.IMBotMetadata = None,
        min_instances: int = None,
    ):
        # This parameter is required.
        self.bot_biz_id = bot_biz_id
        # This parameter is required.
        self.bot_biz_secret = bot_biz_secret
        # This parameter is required.
        self.bot_biz_type = bot_biz_type
        # standard、custom；不传时可能继承租户已有部署模式
        self.bot_mode = bot_mode
        # This parameter is required.
        self.bot_name = bot_name
        # Bot 描述信息
        self.description = description
        # botMode 为 standard 时条件必填；custom 模式不进行标准运行时绑定校验
        self.metadata = metadata
        # FC 最小实例数，≥ 1；与租户账号级配置相关
        self.min_instances = min_instances

    def validate(self):
        if self.metadata:
            self.metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bot_biz_id is not None:
            result['botBizId'] = self.bot_biz_id

        if self.bot_biz_secret is not None:
            result['botBizSecret'] = self.bot_biz_secret

        if self.bot_biz_type is not None:
            result['botBizType'] = self.bot_biz_type

        if self.bot_mode is not None:
            result['botMode'] = self.bot_mode

        if self.bot_name is not None:
            result['botName'] = self.bot_name

        if self.description is not None:
            result['description'] = self.description

        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()

        if self.min_instances is not None:
            result['minInstances'] = self.min_instances

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('botBizId') is not None:
            self.bot_biz_id = m.get('botBizId')

        if m.get('botBizSecret') is not None:
            self.bot_biz_secret = m.get('botBizSecret')

        if m.get('botBizType') is not None:
            self.bot_biz_type = m.get('botBizType')

        if m.get('botMode') is not None:
            self.bot_mode = m.get('botMode')

        if m.get('botName') is not None:
            self.bot_name = m.get('botName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('metadata') is not None:
            temp_model = main_models.IMBotMetadata()
            self.metadata = temp_model.from_map(m.get('metadata'))

        if m.get('minInstances') is not None:
            self.min_instances = m.get('minInstances')

        return self

