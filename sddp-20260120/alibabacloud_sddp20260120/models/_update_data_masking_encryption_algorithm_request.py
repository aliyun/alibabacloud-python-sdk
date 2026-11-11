# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataMaskingEncryptionAlgorithmRequest(DaraModel):
    def __init__(
        self,
        encryption_algorithm: str = None,
        encryption_key_id: str = None,
        instance_id: str = None,
        lang: str = None,
        product_code: str = None,
        product_id: int = None,
    ):
        # The name of the instance-level column encryption algorithm. Select an available algorithm from ListDataMaskingEncryptionAlgorithms.
        self.encryption_algorithm = encryption_algorithm
        # The identifier of the Key Management Service (KMS) key. You can obtain it from Items[].KeyId in the response of ListKmsKeys. Provide this parameter when using a KMS key. Do not pass this parameter in local key scenarios.
        self.encryption_key_id = encryption_key_id
        # The database instance identity. You can obtain it from Items[].InstanceId in the response of ListDataMaskingInstances.
        self.instance_id = instance_id
        # The language of the response description. Valid values:
        # - zh: Chinese.
        # - en: English.
        self.lang = lang
        # The code of the cloud service. Column encryption supports ApsaraDB RDS, PolarDB, and PolarDB-X 2.0. If ProductId is also provided, the two parameters must match.
        self.product_code = product_code
        # The identifier of the cloud service type. Valid values:
        # - 5: ApsaraDB RDS.
        # - 8: PolarDB.
        # - 27: PolarDB-X 2.0.
        # If specified together with ProductCode, the values must match.
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encryption_algorithm is not None:
            result['EncryptionAlgorithm'] = self.encryption_algorithm

        if self.encryption_key_id is not None:
            result['EncryptionKeyId'] = self.encryption_key_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptionAlgorithm') is not None:
            self.encryption_algorithm = m.get('EncryptionAlgorithm')

        if m.get('EncryptionKeyId') is not None:
            self.encryption_key_id = m.get('EncryptionKeyId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        return self

