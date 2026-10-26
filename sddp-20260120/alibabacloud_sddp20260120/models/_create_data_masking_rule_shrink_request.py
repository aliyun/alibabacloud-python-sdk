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
        # The name of the column encryption algorithm. The availability of AES_128_GCM, AES_256_GCM, and SM4_128_GCM depends on the instance. Select an available algorithm from ListDataMaskingEncryptionAlgorithms.
        self.enc_algorithm = enc_algorithm
        # The identifier of the Key Management Service (KMS) key. You can obtain it from Items[].KeyId in the response of the ListKmsKeys operation. Provide this parameter when you use a KMS key. Do not pass this parameter in local key scenarios.
        self.encryption_key_id = encryption_key_id
        # The key mode. Valid values:
        # - client_key: local key
        # - kms_key: KMS key
        # When you use kms_key, you must specify EncryptionKeyId.
        self.encryption_key_mode = encryption_key_mode
        # The type of the database engine. The value must be consistent with the EngineType of the target instance, such as MySQL or PostgreSQL.
        self.engine_type = engine_type
        # The expiration time of the plaintext permission. The value is a UNIX timestamp in milliseconds since 00:00:00 UTC on January 1, 1970. Specify this parameter only when ExpireTimeOperation is set to SET. The value must be later than the current time and no greater than 2145953410000. The server saves the value with second precision. Do not specify this parameter when ExpireTimeOperation is set to PRESERVE or CLEAR.
        self.expire_time = expire_time
        # The processing method for the permission expiration time. Valid values:
        # - PRESERVE: retains the original expiration time.
        # - CLEAR: clears the expiration time.
        # - SET: sets ExpireTime.
        # Default value: PRESERVE. Only fullAccess supports setting a validity period.
        self.expire_time_operation = expire_time_operation
        # The instance identity. You can obtain it from Items[].InstanceId in the response of the ListDataMaskingInstances operation.
        self.instance_id = instance_id
        # The language of the response description. Valid values:
        # - zh: Chinese
        # - en: English
        self.lang = lang
        # The code of the cloud service. Column encryption supports RDS, POLARDB, and PolarDBX2. If ProductId is also passed, the two must correspond to each other.
        self.product_code = product_code
        # The identifier of the cloud service type. Valid values:
        # - 5: RDS
        # - 8: POLARDB
        # - 27: PolarDBX2
        # When specified together with ProductCode, the values must correspond to each other.
        self.product_id = product_id
        # The identifier of the associated risk handling record. You do not need to specify this parameter in the standard column encryption creation process.
        self.risk_handle_id = risk_handle_id
        # The list of column encryption targets grouped by database and table.
        self.sub_rule_list_shrink = sub_rule_list_shrink
        # The list of database accounts to which the fullAccess plaintext permission is granted. The accounts must belong to the target instance.
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

