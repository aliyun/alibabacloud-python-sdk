# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataMaskingRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        enc_algorithm: str = None,
        encryption_key_id: str = None,
        encryption_key_mode: str = None,
        engine_type: str = None,
        expire_time: int = None,
        expire_time_operation: str = None,
        instance_id: str = None,
        lang: str = None,
        product_code: str = None,
        product_id: int = None,
        risk_handle_id: int = None,
        sub_rule_list_shrink: str = None,
        user_list_shrink: str = None,
    ):
        self.enc_algorithm = enc_algorithm
        self.encryption_key_id = encryption_key_id
        self.encryption_key_mode = encryption_key_mode
        self.engine_type = engine_type
        self.expire_time = expire_time
        self.expire_time_operation = expire_time_operation
        self.instance_id = instance_id
        self.lang = lang
        self.product_code = product_code
        self.product_id = product_id
        self.risk_handle_id = risk_handle_id
        self.sub_rule_list_shrink = sub_rule_list_shrink
        self.user_list_shrink = user_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enc_algorithm is not None:
            result['EncAlgorithm'] = self.enc_algorithm

        if self.encryption_key_id is not None:
            result['EncryptionKeyId'] = self.encryption_key_id

        if self.encryption_key_mode is not None:
            result['EncryptionKeyMode'] = self.encryption_key_mode

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expire_time_operation is not None:
            result['ExpireTimeOperation'] = self.expire_time_operation

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.risk_handle_id is not None:
            result['RiskHandleId'] = self.risk_handle_id

        if self.sub_rule_list_shrink is not None:
            result['SubRuleList'] = self.sub_rule_list_shrink

        if self.user_list_shrink is not None:
            result['UserList'] = self.user_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncAlgorithm') is not None:
            self.enc_algorithm = m.get('EncAlgorithm')

        if m.get('EncryptionKeyId') is not None:
            self.encryption_key_id = m.get('EncryptionKeyId')

        if m.get('EncryptionKeyMode') is not None:
            self.encryption_key_mode = m.get('EncryptionKeyMode')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ExpireTimeOperation') is not None:
            self.expire_time_operation = m.get('ExpireTimeOperation')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RiskHandleId') is not None:
            self.risk_handle_id = m.get('RiskHandleId')

        if m.get('SubRuleList') is not None:
            self.sub_rule_list_shrink = m.get('SubRuleList')

        if m.get('UserList') is not None:
            self.user_list_shrink = m.get('UserList')

        return self

