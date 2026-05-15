# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateConsumerAPIKeyOutput(DaraModel):
    def __init__(
        self,
        active: bool = None,
        api_key: str = None,
        consumer_api_key_id: str = None,
        created_at: str = None,
        description: str = None,
        last_updated_at: str = None,
        masked_key: str = None,
        model_connection_id: str = None,
    ):
        # 密钥是否启用
        self.active = active
        # 完整的API密钥明文，仅在创建时返回一次，请妥善保存
        self.api_key = api_key
        # 消费者API密钥的唯一标识符
        self.consumer_api_key_id = consumer_api_key_id
        # 创建时间，采用ISO 8601格式
        self.created_at = created_at
        # 消费者API密钥的描述信息
        self.description = description
        # 更新时间，采用ISO 8601格式
        self.last_updated_at = last_updated_at
        # API密钥的掩码展示形式
        self.masked_key = masked_key
        # 关联的模型连接标识符
        self.model_connection_id = model_connection_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['active'] = self.active

        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.consumer_api_key_id is not None:
            result['consumerApiKeyId'] = self.consumer_api_key_id

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at

        if self.masked_key is not None:
            result['maskedKey'] = self.masked_key

        if self.model_connection_id is not None:
            result['modelConnectionId'] = self.model_connection_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')

        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('consumerApiKeyId') is not None:
            self.consumer_api_key_id = m.get('consumerApiKeyId')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')

        if m.get('maskedKey') is not None:
            self.masked_key = m.get('maskedKey')

        if m.get('modelConnectionId') is not None:
            self.model_connection_id = m.get('modelConnectionId')

        return self

