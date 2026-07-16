# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListKeysRequest(DaraModel):
    def __init__(
        self,
        filters: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # A filter for master keys. The filter consists of 0 to 10 key-value pairs.
        # 
        # - Key
        # 
        #   - Description: The property to filter.
        # 
        #   - Type: String.
        # 
        # - Values
        # 
        #   - Description: The value to be included after filtering.
        # 
        #   - Type: String array.
        # 
        #   - Length: 0 to 10.
        # 
        # Valid values:
        # 
        # - If \\`Key\\` is set to \\`KeyState\\`, it specifies the key status. Valid values for \\`Value\\` are \\`Enabled\\`, \\`Disabled\\`, \\`PendingDeletion\\`, and \\`PendingImport\\`.
        # 
        # - If \\`Key\\` is set to \\`KeySpec\\`, it specifies the key type. Valid values for \\`Value\\` are \\`Aliyun_AES_256\\`, \\`Aliyun_SM4\\`, \\`RSA_2048\\`, \\`EC_P256\\`, \\`EC_P256K\\`, \\`EC_SM2\\`, and \\`Aliyun_SM4\\`.<br> Note: You can create keys of the \\`EC_SM2\\` and \\`Aliyun_SM4\\` types only in regions that support managed HSMs and have passed the compliance assessment of the Office of State Commercial Cryptography Administration (OSCCA). For more information about the supported regions, see [Supported regions](https://help.aliyun.com/document_detail/125803.html). If you specify \\`EC_SM2\\` or \\`Aliyun_SM4\\` in a region that does not support these key types, the parameters are ignored.<br>
        # 
        # - If \\`Key\\` is set to \\`KeyUsage\\`, it specifies the key usage. Valid values for \\`Value\\` are \\`ENCRYPT/DECRYPT\\` (for data encryption and decryption) and \\`SIGN/VERIFY\\` (for generating and verifying digital signatures).
        # 
        # - If \\`Key\\` is set to \\`ProtectionLevel\\`, it specifies the protection level of the key. Valid values for \\`Value\\` are \\`SOFTWARE\\` and \\`HSM\\`.<br> Note: The HSM protection level is supported only in specific regions. For more information about the supported regions, see [Supported regions](https://help.aliyun.com/document_detail/125803.html). If you specify \\`HSM\\` in a region that does not support it, the parameter is ignored.<br>
        # 
        # - If \\`Key\\` is set to \\`CreatorType\\`, it specifies the creator type. Valid values for \\`Value\\` are \\`User\\` (returns master keys created by users) and \\`Service\\` (returns master keys that are automatically created by other Alibaba Cloud services based on your authorization).
        # 
        # - If \\`Key\\` is set to \\`DKMSInstanceId\\`, it specifies the ID of the KMS instance. Set \\`Value\\` as needed.
        # 
        # - If \\`Key\\` is set to \\`keyId\\`, it specifies the key ID. Set \\`Value\\` as needed.
        # 
        # - If \\`Key\\` is set to \\`AliasName\\`, it specifies the key alias. Set \\`Value\\` as needed.
        # 
        # - If \\`Key\\` is set to \\`Creator\\`, it specifies the key creator. Set \\`Value\\` as needed.
        # 
        # - If \\`Key\\` is set to \\`TagKey\\`, it specifies the key of a key tag. Set \\`Value\\` as needed.
        # 
        # - If \\`Key\\` is set to \\`TagValue\\`, it specifies the value of a key tag. Set \\`Value\\` as needed.
        # 
        # The logical relationship between different keys in \\`Filters\\` is \\`AND\\`. The logical relationship between multiple values for the same key is \\`OR\\`. For example, if you enter `[ {"Key":"KeyState", "Values":["Enabled","Disabled"]}, {"Key":"KeyState", "Values":["PendingDeletion"]}, {"Key":"KeySpec", "Values":["Aliyun_AES_256"]} ]`, the semantics are: `(KeyState=Enabled OR KeyState=Disabled OR KeyState=PendingDeletion) AND (KeySpec=Aliyun_AES_256)`.
        self.filters = filters
        # The page number.<br> Valid values: greater than 0.<br> Default value: 1.<br><br>
        self.page_number = page_number
        # The number of entries to return on each page.<br> Valid values: 1 to 100.<br> Default value: 10.<br><br>
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filters is not None:
            result['Filters'] = self.filters

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

