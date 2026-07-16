# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSecretsRequest(DaraModel):
    def __init__(
        self,
        fetch_tags: str = None,
        filters: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # Specifies whether to return resource tags for each secret. Valid values:
        # 
        # - `true`: Resource tags are returned.
        # 
        # - `false` (default): Resource tags are not returned.
        self.fetch_tags = fetch_tags
        # Filters secrets based on specified conditions. The value is a list of up to 10 key-value pairs. When you filter by tag, the query returns a maximum of 4,000 resources. If more than 4,000 resources match the filter, call the [ListResourceTags](https://help.aliyun.com/document_detail/120090.html) operation.
        # 
        # - Key
        # 
        #   - Description: The filter property.
        # 
        #   - Type: String.
        # 
        # - Values
        # 
        #   - Description: The filter value.
        # 
        #   - Type: String.
        # 
        #   - You can specify up to 10 items.
        # 
        # Valid values for Key:
        # 
        # - Set `Key` to **SecretName** to filter by secret name.
        # 
        # - Set `Key` to **Description** to filter by secret description.
        # 
        # - Set `Key` to **TagKey** to filter by tag key.
        # 
        # - Set `Key` to **TagValue** to filter by tag value.
        # 
        # - Set `Key` to **DKMSInstanceId** to filter by KMS instance ID.
        # 
        # - Set Key to **SecretType** to filter by secret type. `Values` can be `Generic`, `RDS`, `Redis`, `RAMCredentials`, `ECS`, or `PolarDB`.
        # 
        # - Set `Key` to **Creator** to filter by the creator of the secret.
        # 
        # If you specify multiple values for a key, the filter applies a logical OR. For example, if you enter `[ {"Key":"SecretName", "Values":["sec1","sec2"]} ]`, this means: `(SecretName=sec1 OR SecretName=sec2)`.
        self.filters = filters
        # The page number.<br>
        # The value must be greater than 0.<br>
        # Default: 1.<br><br>
        self.page_number = page_number
        # The page size.<br>
        # The value must be between 1 and 100.<br>
        # Default: 10.<br><br>
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fetch_tags is not None:
            result['FetchTags'] = self.fetch_tags

        if self.filters is not None:
            result['Filters'] = self.filters

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FetchTags') is not None:
            self.fetch_tags = m.get('FetchTags')

        if m.get('Filters') is not None:
            self.filters = m.get('Filters')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

